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

    module_args = dict(
        name=dict(type='str', required=True),
        description=dict(type='str', required=False, default='generic'),
        public_key=dict(type='str', required=True),
        secret_key=dict(type='str', required=True, no_log=True),
        state=dict(required=True, choices=['present', 'absent'])
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        return result


def create_api_key(name, public_key, secret_key, description):
    payload = dict(
        name=name,
        publicValue=public_key,
        secretValue=secret_key,
        description=description
    )
    try:
        requests.post(API_KEYS_URL, data=payload)
    except HTTPError as error:
        module.fail_json(msg='Failed to create API key: {err}'.format(err=error), **result)
    else:
        module.exit_json(
            changed=True,
            msg='Created API Key {name}'.format(
                name=payload.name
            ), **result
        )


def delete_api_key(key_name):
    removes = []
    api_keys_get = requests.get(API_KEYS_URL)
    for api_key in api_keys_get.json()['data']:
        ids = api_key['id'], api_key['name']
        removes.append(ids)
        for i in removes:
            if i[1] == key_name:
                key_name = i[0]
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
                    module.fail_json(msg='Failed to delete API key: {err}'.format(err=error), **result)
                else:
                    module.exit_json(
                        changed=True,
                        msg='Deleted API Key {name}'.format(
                            name=key_name
                        ), **result
                    )


def get_api_key(search):
    api_keys = requests.get(API_KEYS_URL).json()['data']
    matched_key = [api_key for api_key in api_keys if api_key['name'] == search]
    if matched_key:
        return matched_key[0]

    return None


if __name__ == '__main__':
    main()
