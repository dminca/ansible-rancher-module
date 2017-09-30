#!/usr/bin/python
from __future__ import (absolute_import, division)
from ansible.module_utils.basic import AnsibleModule
import requests

__metaclass__ = type

DEFAULT_RANCHER_HOST = 'http://localhost:8080'
API_URL = '{host}/v2-beta/'.format(host=DEFAULT_RANCHER_HOST)


class RancherProjectModule(object):
    """Rancher Environments (or Project in Rancher API slang)
       CRUD.
    """
    def __init__(self):
        self.module = AnsibleModule(
            argument_spec=dict(
                name
                description
                members
            )
        )
