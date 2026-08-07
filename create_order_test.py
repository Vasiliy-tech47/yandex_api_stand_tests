import sender_stand_request
import data

def test_get_order_by_track_success():
    #Шаг 1: Выполнить запрос на создание заказа
    response_create = sender_stand_request.post_new_order(data.order_body)
    
    #Шаг 2: Сохранить номер трека заказа из ответа
    track_number = response_create.json()["track"]
    
    #Шаг 3: Выполнить запрос на получение заказа по треку
    response_get = sender_stand_request.get_order_by_track(track_number)
    
    #Шаг 4: Проверить, что код ответа равен 200
    assert response_get.status_code == 200