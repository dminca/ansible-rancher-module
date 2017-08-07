#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
from .module_utils.rancher.rancher import RancherModule

import requests

class RancherApiKeyModule(RancherModule):
    """The rancher_api_key module for Ansible"""
    def __init__(self):
        super(RancherApiKeyModule, self).__init__(
            module = AnsibleModule(
                argument_spec=RancherModule.argument_spec()
            )
        )

        self.name = self.module.params['name']
        self.description = self.module.params['description']
        self.public_key = self.module.params['public_key']
        self.secret_key = self.module.params['secret_key']
        self.state = self.module.params['state']

    def state_present(self):
        api_key = self._get_api_key()

        if api_key:
            self.module.exit_json(
                changed=False,
                msg='API Key already exists',
                api_key=self._api_key_to_dict(api_key)
            )

        api_key = self._create_api_key()

        self.module.exit_json(
            changed=True,
            msg='Created API Key {key}'.format(key=self.name),
            api_key=self._api_key_to_dict(api_key)
        )

    def state_absent(self):
        api_key = self._get_api_key()

        if not api_key:
            self.module.exit_json(
                changed=False,
                msg='API Key {key} does not exist'.format(key=self.name),
                api_key=self._api_key_to_dict(api_key)
            )

            # TODO: do we really need this?
            return

        self._delete_api_key(api_key)


    def _api_key_to_dict(self, api_key):
        api_key_dict = dict(
            id=api_key['id'],
            name=api_key['name'],
            description=api_key['description']
        )

        return api_key_dict

    def _create_api_key(self):
        payload = dict(
            name=self.name,
            publicValue=self.public_key,
            secretValue=self.secret_key,
            description=self.description
        )
        try:
            requests.post(API_KEYS_URL, data=payload)
        except HTTPError as error:
            self.module.fail_json(msg='Failed to create API key: {err}'.format(err=error), **result)
        else:
            self.module.exit_json(
                changed=True,
                msg='Created API Key {name}'.format(
                    name=payload.name
                ), **result
            )

    def _delete_api_key(self, api_key):
        removes = []
        api_keys_get = requests.get(API_KEYS_URL)
        for api_key in api_keys_get.json()['data']:
            ids = self.id, self.name
            removes.append(ids)
            for i in removes:
                if i[1] == api_key:
                    api_key = i[0]
                    try:
                        requests.post("{url}/{key_id}?action=deactivate".format(
                            url=API_KEYS_URL,
                            key_id=api_key
                        ))
                        time.sleep(1) # needs time to deactivate
                        requests.delete("{url}/{key_id}".format(
                            url=API_KEYS_URL,
                            key_id=api_key
                        ))
                    except HTTPError as error:
                        self.module.fail_json(
                            msg='Failed to delete API key: {err}'.format(
                                err=error
                            ), **result)
                    else:
                        self.module.exit_json(
                            changed=True,
                            msg='Deleted API Key {name}'.format(
                                name=api_key
                            ), **result
                        )

    def _get_api_key(self):
        api_keys = requests.get(API_KEYS_URL).json()['data']
        matched_key = [api_key for api_key in api_keys if api_key['name'] == self.name]
        if matched_key:
            return matched_key[0]

        return None

def main():
    DEFAULT_RANCHER_HOST = 'http://localhost:8080'
    API_KEYS_URL = '{host}/v2-beta/apiKeys'.format(host=DEFAULT_RANCHER_HOST)

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            description=dict(type='str', required=False, default='generic'),
            public_key=dict(type='str', required=True),
            secret_key=dict(type='str', required=True, no_log=True),
            state=dict(choices=['present', 'absent'], default='present')
        ), supports_check_mode=True
    )

    def _create_api_key(self):
        payload = dict(
            name=self.name,
            publicValue=self.public_key,
            secretValue=self.secret_key,
            description=self.description
        )
        try:
            requests.post(API_KEYS_URL, data=payload)
        except HTTPError as error:
            self.module.fail_json(msg='Failed to create API key: {err}'.format(err=error), **result)
        else:
            self.module.exit_json(
                changed=True,
                msg='Created API Key {name}'.format(
                    name=payload.name
                ), **result
            )

if __name__ == '__main__':
    main()
