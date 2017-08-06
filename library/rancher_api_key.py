#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
from time import sleep

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

def create_api_key(name, public_key, secret_key, description='default'):
    payload = dict(
        name=name,
        publicValue=public_key,
        secretValue=secret_key,
        description=description
    )
    try:
        requests.post(API_KEYS_URL, data=payload)
    except HTTPError as error:
        raise error
    else:
        return True


def delete_api_key(key_name):
    removes = []
    api_keys_get = requests.get(API_KEYS_URL)
    for api_key in api_keys_get.json()['data']:
        ids = api_key['id'], api_key['name']
        removes.append(ids)
        for i in removes:
            if i[1] == key_name:
                key_name = i[0]
                # first deactivate
                try:
                    requests.post("{url}/{key_id}?action=deactivate".format(
                        url=API_KEYS_URL,
                        key_id=key_name
                    ))
                    time.sleep(1) # needs time to deactivate
                    requests.delete("{url}/{key_id}".format(
                        url=API_KEYS_URL,
                        key_id=key_name
                    ))
                except HTTPError as error:
                    raise error
                else:
                    return True

def update_api_key():
    pass


def get_api_keys():
    api_keys = []
    api_keys_get = requests.get(API_KEYS_URL)
    for api_key in api_keys_get.json()['data']:
        ids = api_key['id'], api_key['name']
        api_keys.append(ids)
    return api_keys


if __name__ == '__main__':
    main()
