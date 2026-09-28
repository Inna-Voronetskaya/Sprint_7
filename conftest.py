import pytest

from api.api_helpers import ApiHelpers
from api.courier_api import CourierApi


@pytest.fixture
def courier():
    courier_data = ApiHelpers.register_new_courier_and_return_login_password()

    if not courier_data:
        pytest.fail("Не удалось создать курьера для теста")

    login, password, first_name = courier_data
    courier_id = ApiHelpers.login_and_get_id(login, password)

    yield {
        "login": login,
        "password": password,
        "firstName": first_name,
        "id": courier_id
    }

    if courier_id:
        CourierApi.delete_courier(courier_id)


@pytest.fixture
def courier_cleaner():
    created_ids = []

    def register(courier_id):
        if courier_id:
            created_ids.append(courier_id)

    yield register

    for courier_id in created_ids:
        CourierApi.delete_courier(courier_id)