# tests/test_get_orders.py

import allure

from api.orders_api import OrdersApi
from config import StatusCodes, ErrorMessages


@allure.feature("Список заказов")
class TestGetOrders:
    """Тесты для ручки GET /api/v1/orders"""

    @allure.title("В тело ответа возвращается список заказов")
    def test_get_orders_returns_list(self):
        response = OrdersApi.get_orders()

        assert response.status_code == StatusCodes.OK
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)

    @allure.title("Список заказов можно отфильтровать по курьеру")
    @allure.description("Для несуществующего курьера → 404 и текст ошибки")
    def test_get_orders_with_courier_filter(self):
        courier_id = 999999
        response = OrdersApi.get_orders(courier_id=courier_id)

        assert response.status_code == StatusCodes.NOT_FOUND
        expected = ErrorMessages.COURIER_ID_NOT_FOUND.format(courier_id=courier_id)
        assert expected in response.json()["message"]