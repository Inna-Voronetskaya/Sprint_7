# api/api_helpers.py

import requests
import random
import string

from config import BASE_URL
from api.courier_api import CourierApi


class ApiHelpers:
    """Готовые сценарии и вспомогательные методы для тестов."""

    @staticmethod
    def register_new_courier_and_return_login_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass

    @staticmethod
    def login_and_get_id(login, password):
        response = CourierApi.login_courier({
            "login": login,
            "password": password
        })
        if response.status_code == 200:
            return response.json().get("id")
        return None