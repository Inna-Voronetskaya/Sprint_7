# tests/test_create_courier.py

import allure
import pytest

from api.courier_api import CourierApi
from api.api_helpers import ApiHelpers
from helpers.data_generator import generate_courier_data
from config import StatusCodes, ERROR_MESSAGES


@allure.feature("Создание курьера")
class TestCreateCourier:
    """Тесты для ручки POST /api/v1/courier"""

    @allure.title("Курьера можно создать")
    @allure.description("Успешное создание курьера → 201 и ok: True")
    def test_create_courier_success(self):
        payload = generate_courier_data()
        response = CourierApi.create_courier(payload)

        assert response.status_code == StatusCodes.CREATED
        assert response.json() == {"ok": True}

        # Уборка: удаляем созданного курьера
        courier_id = ApiHelpers.login_and_get_id(payload["login"], payload["password"])
        if courier_id:
            CourierApi.delete_courier(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Второй курьер с тем же логином → 409 и текст ошибки")
    def test_create_duplicate_courier_returns_error(self):
        payload = generate_courier_data()

        # Первый курьер — успешно
        response1 = CourierApi.create_courier(payload)
        assert response1.status_code == StatusCodes.CREATED

        # Второй с тем же логином — ошибка 409
        response2 = CourierApi.create_courier(payload)
        assert response2.status_code == StatusCodes.CONFLICT
        assert ERROR_MESSAGES["login_already_used"] in response2.json()["message"]

        # Уборка
        courier_id = ApiHelpers.login_and_get_id(payload["login"], payload["password"])
        if courier_id:
            CourierApi.delete_courier(courier_id)

    @allure.title("Если одного из обязательных полей нет → ошибка 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field(self, missing_field):
        payload = generate_courier_data()
        payload.pop(missing_field)   # удаляем одно из обязательных полей

        response = CourierApi.create_courier(payload)

        assert response.status_code == StatusCodes.BAD_REQUEST
        assert ERROR_MESSAGES["insufficient_creation_data"] in response.json()["message"]