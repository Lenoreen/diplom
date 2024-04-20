import requests
import config
import data


def test_order_by_track():
    track_number = requests.post(config.URL + config.CREATE_ORDER,
                                 json=data.order_body).json()['track']
    requests.get(config.URL + config.TRACK_ORDER, params={'t': track_number})
    response = requests.get(config.URL + config.TRACK_ORDER, params={'t': track_number})

    assert response.status_code == 200

# Елена Плисова, 15-я когорта - финальный проект. Инженер по тестированию плюс
