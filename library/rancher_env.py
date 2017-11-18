#!/usr/bin/python
from __future__ import (absolute_import, division)

import requests
from ansible.module_utils.basic import AnsibleModule

__metaclass__ = type

DEFAULT_RANCHER_HOST = 'http://localhost:8080'
API_URL = '{host}/v2-beta/projects'.format(host=DEFAULT_RANCHER_HOST)


class RancherEnvironmentModule(object):
    """Rancher Environments (or Project in Rancher API slang)
       CRUD.
    """
    def __init__(self):
        self.module = AnsibleModule(
            argument_spec=dict(
                name=dict(type='str', required=True),
                description=dict(type='str', default='generic'),
                members=dict(type='list'),
                state=dict(choices=[
                    'present',
                    'absent'
                ], default='present')
            ), supports_check_mode=True
        )

        self.name = self.module.params['name']
        self.description = self.module.params['description']
        self.members = self.module.params['members']
        self.state = self.module.params['state']

    def _create_environment(self):
        payload = dict(
            name=self.name,
            description=self.description,
            members=self.members
        )

    def _delete_environment(self):
        pass

    def _get_environment(self):
        pass

    def _get_project_member(self, name):
        """
        Return a Project Member ID from a name
        :param name: string
        :return: string
        """
        pass


def main():
    RancherEnvironmentModule()


if __name__ == '__main__':
    main()
