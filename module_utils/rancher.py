#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
from time import sleep
try:
    import requests
except ImportError:
    REQUESTS_FOUND = True
else:
    REQUESTS_FOUND = False

DEFAULT_RANCHER_HOST = 'http://localhost:8080'
API_KEYS_URL = '{host}/v2-beta/apiKeys'.format(host=DEFAULT_RANCHER_HOST)

class RancherModule(object):
    """Base class containing utilities for the Rancher Module"""
    def __init__(self, module):
        """
        Create a new RancherModule

        Will fail if requests module is not present.
        :param module: The underlying Ansible module
        :type module: AnsibleModule
        """
        self.module = module

        if not REQUESTS_FOUND:
            self.module.fail_json(msg='requests is required for this module.')

    @staticmethod
    def argument_spec(**additional_arg_spec):
        spec = dict(
            name=dict(type='str', required=True),
            description=dict(type='str', required=False, default='generic'),
            public_key=dict(type='str', required=True),
            secret_key=dict(type='str', required=True, no_log=True),
            state=dict(choices=['present', 'absent'], default='present')
        )

        if additional_arg_spec:
            spec.update(additional_arg_spec)

        return spec
