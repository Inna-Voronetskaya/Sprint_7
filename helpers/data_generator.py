# helpers/data_generator.py
import random
import string


def generate_random_string(length=10):
    """Генерирует случайную строку из букв нижнего регистра."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_courier_data():
    """Словарь с данными нового курьера."""
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }


def generate_courier_login_data(login=None, password=None):
    """Данные для авторизации курьера."""
    return {
        "login": login if login else generate_random_string(10),
        "password": password if password else generate_random_string(10)
    }


def generate_order_data(color=None):
    """
    Генерирует тело запроса для создания заказа.
    :param color: список цветов, например ["BLACK"] или ["BLACK", "GREY"].
                  Если None — цвет не указан (пустой список).
    """
    return {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, ул. Ленина, д. 1",
        "metroStation": 4,
        "phone": "+7 999 999 99 99",
        "rentTime": 3,
        "deliveryDate": "2025-12-31",
        "comment": "Позвоните перед доставкой",
        "color": color if color is not None else []
    }