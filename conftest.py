# conftest.py

import pytest

from api.api_helpers import ApiHelpers
from api.courier_api import CourierApi


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