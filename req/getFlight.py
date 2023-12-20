import requests
import os
from db.models import ApiRequest


def load_env_variables(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            os.environ[key] = value


def get_flight(ApiRequest):
    load_env_variables('.env')
    api_key = os.environ.get('API_KEY')

    code_dest = requests.get(f'https://api.flightapi.io/iata/{api_key}?name={ApiRequest.destination_city}&type=airport')

    code_dep = requests.get(f'https://api.flightapi.io/iata/{api_key}?name={ApiRequest.departure_city}&type=airport')

    print(code_dest.json())
    print(code_dep.json())

    resp = requests.get(f'https://api.flightapi.io/onewaytrip/{api_key}/{code_dest.json()['data'][0]['iata']}/'
                        f'{code_dep.json()['data'][0]['iata']}/{ApiRequest.date}/{ApiRequest.numberOfAdults}/0/0/'
                        f'{ApiRequest.cabinClass}'
                        f'/USD')
    return resp
