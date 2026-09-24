# tests/test_create_order.py

import allure
import pytest

from api.orders_api import OrdersApi
from helpers.data_generator import generate_order_data
from config import StatusCodes


@allure.feature("Создание заказа")
class TestCreateOrder:
    """Тесты для ручки POST /api/v1/orders"""

    @allure.title("Создание заказа с разными комбинациями цветов")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None,
    ], ids=[
        "black_only",
        "grey_only",
        "both_colors",
        "no_color",
    ])
    def test_create_order_with_colors(self, color):
        payload = generate_order_data(color=color)
        response = OrdersApi.create_order(payload)

        assert response.status_code == StatusCodes.CREATED
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)
        assert response.json()["track"] > 0