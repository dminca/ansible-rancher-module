#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import json

try:
    import requests
except ImportError:
    REQUESTS_FOUND = True
else:
    REQUESTS_FOUND = False



if __name__ == '__main__':
    main()
