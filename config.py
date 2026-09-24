# config.py


class Urls:
    """Адреса сервиса Яндекс Самокат."""
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER = f'{BASE_URL}/api/v1/courier'
    COURIER_LOGIN = f'{BASE_URL}/api/v1/courier/login'
    ORDERS = f'{BASE_URL}/api/v1/orders'
    ORDERS_TRACK = f'{BASE_URL}/api/v1/orders/track'
    ORDERS_ACCEPT = f'{BASE_URL}/api/v1/orders/accept'
    ORDERS_CANCEL = f'{BASE_URL}/api/v1/orders/cancel'


class StatusCodes:
    """Коды ответов API."""
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409


class ErrorMessages:
    """Тексты ошибок, которые возвращает API."""
    # Создание курьера
    LOGIN_ALREADY_USED = "Этот логин уже используется. Попробуйте другой."
    INSUFFICIENT_CREATION_DATA = "Недостаточно данных для создания учетной записи"

    # Авторизация курьера
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    INSUFFICIENT_LOGIN_DATA = "Недостаточно данных для входа"

    # Работа с курьером по id
    COURIER_NOT_EXIST = "Курьера с таким id нет."
    COURIER_ID_NOT_FOUND = "Курьер с идентификатором {courier_id} не найден"