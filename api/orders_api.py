# api/orders_api.py

import allure
import requests
from config import Urls

TIMEOUT = 30


class OrdersApi:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        """POST /api/v1/orders — создание заказа."""
        return requests.post(Urls.ORDERS, json=payload, timeout=TIMEOUT)

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders(courier_id=None, nearest_station=None, limit=30, page=0):
        """GET /api/v1/orders — список заказов с фильтрами."""
        params = {"limit": limit, "page": page}
        if courier_id:
            params["courierId"] = courier_id
        if nearest_station:
            params["nearestStation"] = nearest_station
        return requests.get(Urls.ORDERS, params=params, timeout=TIMEOUT)

    @staticmethod
    @allure.step("Получение заказа по track={track}")
    def get_order_by_track(track):
        """GET /api/v1/orders/track?t={track} — получить заказ по номеру."""
        return requests.get(Urls.ORDERS_TRACK, params={'t': track}, timeout=TIMEOUT)

    @staticmethod
    @allure.step("Принятие заказа {order_id} курьером {courier_id}")
    def accept_order(order_id, courier_id):
        """PUT /api/v1/orders/accept/{id}?courierId={courier_id}"""
        return requests.put(
            f'{Urls.ORDERS_ACCEPT}/{order_id}',
            params={'courierId': courier_id},
            timeout=TIMEOUT
        )

    @staticmethod
    @allure.step("Отмена заказа по track={track}")
    def cancel_order(track):
        """PUT /api/v1/orders/cancel?track={track}"""
        return requests.put(Urls.ORDERS_CANCEL, params={'track': track}, timeout=TIMEOUT)