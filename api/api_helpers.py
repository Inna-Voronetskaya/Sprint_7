# api/api_helpers.py

import allure
import requests
import random
import string

from config import Urls
from api.courier_api import CourierApi


class ApiHelpers:

    @staticmethod
    @allure.step("Регистрация нового курьера")
    def register_new_courier_and_return_login_password():
        """Метод из задания: регистрирует нового курьера."""
        def generate_random_string(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))

        login_pass = []
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(Urls.COURIER, data=payload, timeout=10)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass

    @staticmethod
    @allure.step("Логин курьера и получение id")
    def login_and_get_id(login, password):
        """Логинит курьера и возвращает его id."""
        response = CourierApi.login_courier({"login": login, "password": password})
        if response.status_code == 200:
            return response.json().get("id")
        return None