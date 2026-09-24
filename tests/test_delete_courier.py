# tests/test_delete_courier.py

import allure

from api.courier_api import CourierApi
from api.api_helpers import ApiHelpers
from config import StatusCodes, ERROR_MESSAGES


@allure.feature("Удаление курьера")
class TestDeleteCourier:
    """Тесты для ручки DELETE /api/v1/courier/{id}"""

    @allure.title("Успешный запрос возвращает ok: true")
    def test_delete_courier_success(self):
        login, password, _ = ApiHelpers.register_new_courier_and_return_login_password()
        courier_id = ApiHelpers.login_and_get_id(login, password)

        response = CourierApi.delete_courier(courier_id)

        assert response.status_code == StatusCodes.OK
        assert response.json() == {"ok": True}

    @allure.title("Неуспешный запрос возвращает ошибку")
    def test_delete_courier_with_nonexistent_id_returns_error(self):
        response = CourierApi.delete_courier(999999)

        assert response.status_code == StatusCodes.NOT_FOUND
        assert ERROR_MESSAGES["courier_not_exist"] in response.json()["message"]

    @allure.title("Запрос без id → ошибка")
    def test_delete_courier_without_id_returns_error(self):
        response = CourierApi.delete_courier("")

        assert response.status_code in (
            StatusCodes.BAD_REQUEST,
            StatusCodes.NOT_FOUND,
        )

    @allure.title("Запрос с несуществующим id → ошибка")
    def test_delete_courier_with_wrong_id_returns_error(self):
        response = CourierApi.delete_courier(0)

        assert response.status_code == StatusCodes.NOT_FOUND