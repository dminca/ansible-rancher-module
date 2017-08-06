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

    api_keys_get = requests.get(API_KEYS_URL)

    for api_key in api_keys_get.json()['data']:
        ids = api_key['id'], api_key['name']
        api_keys.append(ids)

    # DELETE API Keys
    removes = []
    search_for = ''
    for api_key in api_keys_get.json()['data']:
        ids = api_key['id'], api_key['name']
        removes.append(ids)
        for i in removes:
            if i[1] == search_for:
                search_for = i[0]
                # first deactivate
                requests.post("{url}/{key_id}?action=deactivate".format(
                    url=API_KEYS_URL,
                    key_id=search_for
                ))
                # now delete
                api_keys_del = requests.delete("{url}/{key_id}".format(
                    url=API_KEYS_URL,
                    key_id=search_for
                ))



if __name__ == '__main__':
    main()
