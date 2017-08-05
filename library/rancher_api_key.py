#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import json

try:
    import requests
except ImportError:
    REQUESTS_FOUND = True
else:
    REQUESTS_FOUND = False


def main():
    API_KEYS_URL = '{protocol}://{url}:{port}/v2-beta/apiKeys'.format(
        protocol='http',
        url='localhost',
        port='8080'
    )

    # CREATE
    payload = {
        "description": "bob test",
        "name": "bob",
        "publicValue": "bobpublickey",
        "secretValue": "bobsecretkey"
    }

    r = requests.post(API_KEYS_URL, data=payload)

    # GET all API Keys
    api_keys = []

    api_keys_req = requests.get(API_KEYS_URL)

    for api_key in api_keys_req.json()['data']:
        ids = api_key['id'], api_key['name']
        api_keys.append(ids)

    # DELETE API Keys
    removes = []



if __name__ == '__main__':
    main()
