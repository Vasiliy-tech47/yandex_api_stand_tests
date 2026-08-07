import requests
import configuration
import data

#Функция для отправки запроса на создание заказа
def post_new_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body
    )

#Функция для получения заказа по его трек-номеру
def get_order_by_track(track_number):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
        params={"t": track_number}
    )