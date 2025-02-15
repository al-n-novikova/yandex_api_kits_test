# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data


# Функция для позитивной проверки
def positive_assert(kit_body_name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = sender_stand_request.get_kit_body (kit_body_name)

    # В переменную kit_response сохраняется результат запроса на создание набора пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201

    # Проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()['name'] == kit_body_name

# Функция для негативной проверки
def negative_assert(kit_body_name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = sender_stand_request.get_kit_body(kit_body_name)
    # В переменную response сохраняется результат запроса на создание пользователя:
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 400
    assert response.status_code == 400

# Функция для негативной проверки без параметров
def negative_assert_no_name(kit_body):
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 400
    assert response.status_code == 400

    # Проверка, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400
    # Проверка текста в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Не все необходимые параметры были переданы"


# Тест 1. Успешное создание набора пользователя
# Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Тест 2. Успешное создание набора пользователя
# Параметр name состоит из 511 символа
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Ошибка 
# Параметр name состоит из пустой строки
def test_create_kit_empty_name_get_error_response():
    negative_assert("")

# Тест 4. Ошибка
# Параметр name состоит из 512 символа
def test_create_kit_512_letter_in_name_get_success_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Успешное создание набора пользователя
# Параметр name состоит из английских символов
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание набора пользователя
# Параметр name состоит из русских символов
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание набора пользователя
# Параметр name со спецсимволом
def test_create_kit_has_special_symbol_letter_in_name_get_success_response():
    positive_assert('"\u2116%@",')

# Тест 8. Успешное создание набора пользователя
# Параметр name с пробелом
def test_create_kit_has_space_letter_in_name_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Успешное создание набора пользователя
# Параметр name с цифрами
def test_create_kit_has_number_letter_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Ошибка 
# В запросе нет параметра name
def test_create_kit_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную kit_body
    # Иначе можно потерять данные из исходного словаря
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)

# Тест 11. Ошибка
# Параметр name число
def test_create_kit_number_type_name_get_error_response():
        negative_assert(123)