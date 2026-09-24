# tests/test_login_courier.py
import allure
import pytest

from api.courier_api import CourierApi
from helpers.data_generator import generate_courier_login_data, generate_random_string
from config import StatusCodes, ERROR_MESSAGES


@allure.feature("Логин курьера")
class TestLoginCourier:
    """Тесты для ручки POST /api/v1/courier/login"""

    @allure.title("Курьер может авторизоваться")
    @allure.description("Успешный логин → 200 и возвращается id курьера")
    def test_login_courier_success(self, courier):
        response = CourierApi.login_courier({
            "login": courier["login"],
            "password": courier["password"]
        })

        assert response.status_code == StatusCodes.OK
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)
        assert response.json()["id"] == courier["id"]

    @allure.title("Если не передать login → ошибка 400")
    def test_login_without_login_field_returns_error(self, courier):
        response = CourierApi.login_courier({
            "password": courier["password"]
        })

        assert response.status_code == StatusCodes.BAD_REQUEST
        assert ERROR_MESSAGES["insufficient_login_data"] in response.json()["message"]

    @allure.title("Если не передать password → ошибка (баг API: 504)")
    @pytest.mark.skip(reason="API возвращает 504 вместо 400 при отсутствии password")
    def test_login_without_password_field_returns_error(self, courier):
        response = CourierApi.login_courier({
            "login": courier["login"]
        })

        assert response.status_code == StatusCodes.BAD_REQUEST
        assert ERROR_MESSAGES["insufficient_login_data"] in response.json()["message"]

    @allure.title("Неверный логин → ошибка 404")
    def test_login_with_wrong_login_returns_error(self, courier):
        response = CourierApi.login_courier({
            "login": generate_random_string(10),
            "password": courier["password"]
        })

        assert response.status_code == StatusCodes.NOT_FOUND
        assert ERROR_MESSAGES["account_not_found"] in response.json()["message"]

    @allure.title("Неверный пароль → ошибка 404")
    def test_login_with_wrong_password_returns_error(self, courier):
        response = CourierApi.login_courier({
            "login": courier["login"],
            "password": generate_random_string(10)
        })

        assert response.status_code == StatusCodes.NOT_FOUND
        assert ERROR_MESSAGES["account_not_found"] in response.json()["message"]

    @allure.title("Несуществующий пользователь → ошибка 404")
    def test_login_with_nonexistent_user_returns_error(self):
        response = CourierApi.login_courier(generate_courier_login_data())

        assert response.status_code == StatusCodes.NOT_FOUND
        assert ERROR_MESSAGES["account_not_found"] in response.json()["message"]