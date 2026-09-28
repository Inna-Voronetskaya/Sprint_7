import allure
import pytest

from api.courier_api import CourierApi
from api.api_helpers import ApiHelpers
from helpers.data_generator import generate_courier_data
from config import StatusCodes, ErrorMessages


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    @allure.description("Успешное создание курьера → 201 и {'ok': True}")
    def test_create_courier_success(self, courier_cleaner):
        payload = generate_courier_data()
        response = CourierApi.create_courier(payload)

        assert response.status_code == StatusCodes.CREATED
        assert response.json() == {"ok": True}

        courier_id = ApiHelpers.login_and_get_id(payload["login"], payload["password"])
        courier_cleaner(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Второй курьер с тем же логином → 409 и текст ошибки")
    def test_create_duplicate_courier_returns_error(self, courier):
        payload = {
            "login": courier["login"],
            "password": courier["password"],
            "firstName": courier["firstName"]
        }
        response = CourierApi.create_courier(payload)

        assert response.status_code == StatusCodes.CONFLICT
        assert ErrorMessages.LOGIN_ALREADY_USED in response.json()["message"]

    @allure.title("Если одного из обязательных полей нет → ошибка 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field(self, missing_field):
        payload = generate_courier_data()
        payload.pop(missing_field)

        response = CourierApi.create_courier(payload)

        assert response.status_code == StatusCodes.BAD_REQUEST
        assert ErrorMessages.INSUFFICIENT_CREATION_DATA in response.json()["message"]