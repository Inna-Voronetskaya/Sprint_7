# tests/test_accept_order.py

import allure

from api.courier_api import CourierApi
from api.orders_api import OrdersApi
from api.api_helpers import ApiHelpers
from helpers.data_generator import generate_order_data
from config import StatusCodes


@allure.feature("Принять заказ")
class TestAcceptOrder:
    """Тесты для ручки PUT /api/v1/orders/accept/{id}"""

    @allure.title("Успешный запрос возвращает ok: true")
    def test_accept_order_success(self):
        # Создаём курьера
        login, password, _ = ApiHelpers.register_new_courier_and_return_login_password()
        courier_id = ApiHelpers.login_and_get_id(login, password)

        # Создаём заказ
        order_response = OrdersApi.create_order(generate_order_data())
        track = order_response.json()["track"]

        # Получаем id заказа по track
        order_info = OrdersApi.get_order_by_track(track)
        order_id = order_info.json()["order"]["id"]

        # Принимаем заказ
        response = OrdersApi.accept_order(order_id, courier_id)

        assert response.status_code == StatusCodes.OK
        assert response.json() == {"ok": True}

        # Уборка: удаляем курьера
        CourierApi.delete_courier(courier_id)

    @allure.title("Без id курьера → ошибка")
    def test_accept_order_without_courier_id_returns_error(self):
        # Создаём заказ
        order_response = OrdersApi.create_order(generate_order_data())
        track = order_response.json()["track"]
        order_id = OrdersApi.get_order_by_track(track).json()["order"]["id"]

        # Без id курьера (пустая строка)
        response = OrdersApi.accept_order(order_id, "")

        assert response.status_code in (
            StatusCodes.BAD_REQUEST,
            StatusCodes.NOT_FOUND,
        )

    @allure.title("Неверный id курьера → ошибка")
    def test_accept_order_with_wrong_courier_id_returns_error(self):
        # Создаём заказ
        order_response = OrdersApi.create_order(generate_order_data())
        track = order_response.json()["track"]
        order_id = OrdersApi.get_order_by_track(track).json()["order"]["id"]

        # Несуществующий id курьера
        response = OrdersApi.accept_order(order_id, 999999)

        assert response.status_code == StatusCodes.NOT_FOUND

    @allure.title("Без id заказа → ошибка")
    def test_accept_order_without_order_id_returns_error(self):
        # Создаём курьера
        login, password, _ = ApiHelpers.register_new_courier_and_return_login_password()
        courier_id = ApiHelpers.login_and_get_id(login, password)

        # Без id заказа (пустая строка)
        response = OrdersApi.accept_order("", courier_id)

        assert response.status_code in (
            StatusCodes.BAD_REQUEST,
            StatusCodes.NOT_FOUND,
        )

        # Уборка
        CourierApi.delete_courier(courier_id)

    @allure.title("Неверный id заказа → ошибка")
    def test_accept_order_with_wrong_order_id_returns_error(self):
        # Создаём курьера
        login, password, _ = ApiHelpers.register_new_courier_and_return_login_password()
        courier_id = ApiHelpers.login_and_get_id(login, password)

        # Несуществующий id заказа
        response = OrdersApi.accept_order(999999, courier_id)

        assert response.status_code == StatusCodes.NOT_FOUND

        # Уборка
        CourierApi.delete_courier(courier_id)