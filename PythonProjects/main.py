import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}

body_create = { 'name':'generate', 'photo_id': -1}
body_change = {'pokemon_id':'138046','name':'generate','photo_id': -1}
body_add = {'pokemon_id':'138046'}
body_knockout = {'pokemon_id':'138013'}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text) # Создать покемона

'''response_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_knockout)
print(response_knockout.text)''' # Отправить покемона в нокаут

response_change = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_change)
print(response_change.text) # Поменять покемону имя и фото

response_add = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_add)
print(response_add.text) # Поймать покемона в покебол
