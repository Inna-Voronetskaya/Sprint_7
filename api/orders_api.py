# api/orders_api.py

import requests
from config import BASE_URL

TIMEOUT = 30      # ← было 10, стало 30


class OrdersApi:

    @staticmethod
    def create_order(payload):
        """POST /api/v1/orders — создание заказа."""
        return requests.post(f'{BASE_URL}/api/v1/orders', json=payload, timeout=TIMEOUT)

    @staticmethod
    def get_orders(courier_id=None, nearest_station=None, limit=30, page=0):
        """GET /api/v1/orders — список заказов с пагинацией и фильтрами."""
        params = {"limit": limit, "page": page}

        if courier_id:
            params["courierId"] = courier_id
        if nearest_station:
            params["nearestStation"] = nearest_station

        return requests.get(f'{BASE_URL}/api/v1/orders', params=params, timeout=TIMEOUT)

    @staticmethod
    def get_order_by_track(track):
        """GET /api/v1/orders/track?t={track} — получить заказ по номеру."""
        return requests.get(f'{BASE_URL}/api/v1/orders/track', params={'t': track}, timeout=TIMEOUT)

    @staticmethod
    def accept_order(order_id, courier_id):
        """PUT /api/v1/orders/accept/{id}?courierId={courier_id} — принять заказ."""
        return requests.put(
            f'{BASE_URL}/api/v1/orders/accept/{order_id}',
            params={'courierId': courier_id},
            timeout=TIMEOUT
        )

    @staticmethod
    def cancel_order(track):
        """PUT /api/v1/orders/cancel?track={track} — отменить заказ."""
        return requests.put(f'{BASE_URL}/api/v1/orders/cancel', params={'track': track}, timeout=TIMEOUT)