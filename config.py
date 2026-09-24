# config.py

BASE_URL = 'https://qa-scooter.praktikum-services.ru'


class StatusCodes:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409


ERROR_MESSAGES = {
    # Создание курьера
    "login_already_used": "Этот логин уже используется. Попробуйте другой.",
    "insufficient_creation_data": "Недостаточно данных для создания учетной записи",

    # Авторизация курьера
    "account_not_found": "Учетная запись не найдена",
    "insufficient_login_data": "Недостаточно данных для входа",

    # DELETE /api/v1/courier/{id} — короткий текст
    "courier_not_exist": "Курьера с таким id нет.",

    # GET /api/v1/orders?courierId=... — длинный текст с id
    "courier_id_not_found": "Курьер с идентификатором {courier_id} не найден",
}