# -*- coding: utf-8 -*-
import requests
from decouple import config


DATASTORE_TOKEN = config('DATASTORE_TOKEN')
DATASTORE_URL = config('DATASTORE_URL')
HEADERS = {'Authorization': f'Token {DATASTORE_TOKEN}'}


def retrieve(object_name, uid=None):
    response = requests.get(f'{DATASTORE_URL}{object_name}', headers=HEADERS)
    data = response.json()['results']

    return data


if __name__ == '__main__':
    groups = retrieve('group')
    for g in groups:
        print("*" * 80)
        print(g["name"])
        print("-" * 80)
        for member in g["members"]:
            print(member["email"])

        print("*" * 80)
