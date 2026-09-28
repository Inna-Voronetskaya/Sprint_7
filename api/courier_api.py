# api/courier_api.py
import allure
import requests
from config import Urls

TIMEOUT = 10


class CourierApi:

    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(payload):
        """POST /api/v1/courier — создание курьера."""
        return requests.post(Urls.COURIER, data=payload, timeout=TIMEOUT)

    @staticmethod
    @allure.step("Логин курьера")
    def login_courier(payload):
        """POST /api/v1/courier/login — авторизация курьера."""
        return requests.post(Urls.COURIER_LOGIN, data=payload, timeout=TIMEOUT)

    @staticmethod
    @allure.step("Удаление курьера с id={courier_id}")
    def delete_courier(courier_id):
        """DELETE /api/v1/courier/{id} — удаление курьера."""
        return requests.delete(f'{Urls.COURIER}/{courier_id}', timeout=TIMEOUT)