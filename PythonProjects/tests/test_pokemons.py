import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}
TRAINER_ID = '8848'


def test_status_code_200():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Сенжи'

@pytest.mark.parametrize('key, value',[('trainer_name','Сенжи'),('id',TRAINER_ID),('city','СанктПетербург')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value
