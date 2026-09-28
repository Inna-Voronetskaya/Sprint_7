# tests/test_get_order_by_track.py

import allure

from api.orders_api import OrdersApi
from helpers.data_generator import generate_order_data
from config import StatusCodes


@allure.feature("Получение заказа по номеру")
class TestGetOrderByTrack:
    """Тесты для ручки GET /api/v1/orders/track"""

    @allure.title("Успешный запрос возвращает объект с заказом")
    def test_get_order_by_track_success(self):
        # Создаём заказ
        order_response = OrdersApi.create_order(generate_order_data())
        track = order_response.json()["track"]

        # Получаем заказ по track
        response = OrdersApi.get_order_by_track(track)

        assert response.status_code == StatusCodes.OK
        assert "order" in response.json()
        assert isinstance(response.json()["order"], dict)

    @allure.title("Запрос без номера заказа → ошибка")
    def test_get_order_without_track_returns_error(self):
        response = OrdersApi.get_order_by_track("")

        assert response.status_code in (
            StatusCodes.BAD_REQUEST,
            StatusCodes.NOT_FOUND,
        )

    @allure.title("Запрос с несуществующим заказом → ошибка")
    def test_get_order_with_nonexistent_track_returns_error(self):
        response = OrdersApi.get_order_by_track(999999999)

        assert response.status_code == StatusCodes.NOT_FOUND