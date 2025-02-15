# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers_user)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body)

# Функция response.json() позволяет получить тело ответа в формате JSON.
# Это полезно для извлечения данных, полученных в результате запроса, 
# особенно когда сервер возвращает полезные данные в формате JSON.
# Здесь мы вызываем эту функцию и записываем ее в переменную auth_token
auth_token = response.json()["authToken"]

# эта функция меняет значения в параметре Authorization
def get_headers_kits (auth_token):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_auth_token = data.headers_kits.copy()
    # изменение значения в поле Authorization
    current_auth_token["Authorization"] = 'Bearer ' + auth_token
    # возвращается новый словарь с нужным значением Authorization
    return current_auth_token

# эта функция меняет значения в параметре name 
def get_kit_body (kit_body_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_kit_body = data.kit_body.copy()
    # изменение значения в поле name
    current_kit_body["name"] = kit_body_name
    # возвращается новый словарь с нужным значением name
    return current_kit_body
 
# Определение функции post_new_client_kit для отправки POST-запроса на создание нового набора пользователя
def post_new_client_kit(kit_body):
    # В переменную headers_kits сохраняется обновлённое тело запроса
    headers_kits = get_headers_kits (auth_token)
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_KITS объединяются для формирования полного URL для запроса
    # json=kit_body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS,
                         json=kit_body,
                         headers=headers_kits)
    
