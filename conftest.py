# conftest.py

import pytest

from api.api_helpers import ApiHelpers
from api.courier_api import CourierApi
from helpers.data_generator import generate_courier_data

@pytest.fixture
def courier():
    """
    Фикстура создаёт нового курьера перед тестом,
    возвращает его данные в тест,
    а после теста — удаляет курьера.
    """
    # === SETUP: подготовка ===
    courier_data = ApiHelpers.register_new_courier_and_return_login_password()

    if not courier_data:
        pytest.fail("Не удалось создать курьера для теста")

    login, password, first_name = courier_data
    courier_id = ApiHelpers.login_and_get_id(login, password)

    # Передаём данные в тест
    yield {
        "login": login,
        "password": password,
        "firstName": first_name,
        "id": courier_id
    }

    # === TEARDOWN: уборка ===
    if courier_id:
        CourierApi.delete_courier(courier_id)

@pytest.fixture
def courier_factory():
    """
    Фабрика курьеров.
    Позволяет тесту создать курьера по требованию.
    Все созданные курьеры удаляются после теста.
    """
    created_ids = []

    def create(payload=None):
        """Создаёт курьера. Возвращает (response, payload)."""
        if payload is None:
            payload = generate_courier_data()
        response = CourierApi.create_courier(payload)
        if response.status_code == 201:
            courier_id = ApiHelpers.login_and_get_id(payload["login"], payload["password"])
            if courier_id:
                created_ids.append(courier_id)
        return response, payload

    yield create

    # Уборка ВСЕХ созданных курьеров — выполняется всегда
    for courier_id in created_ids:
        CourierApi.delete_courier(courier_id)