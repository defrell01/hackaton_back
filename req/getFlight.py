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
    resp = requests.get(f'https://api.flightapi.io/onewaytrip/{api_key}/{ApiRequest.departureCode}/'
                        f'{ApiRequest.arrivalCode}/{ApiRequest.date}/{ApiRequest.numberOfAdults}/0/0/'
                        f'{ApiRequest.cabinClass}'
                        f'/USD')
    return resp
