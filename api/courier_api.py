# api/courier_api.py
import requests
from config import BASE_URL


class CourierApi:

    @staticmethod
    def create_courier(payload):
        return requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

    @staticmethod
    def login_courier(payload):
        return requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{BASE_URL}/api/v1/courier/{courier_id}')