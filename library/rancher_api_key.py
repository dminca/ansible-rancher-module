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
    r = requests.get("http://localhost:8080/v2-beta")
    api_keys_url = r.json()['links']['apiKeys']
    api_keys = requests.get(r.json()['links']['apiKeys'])

if __name__ == '__main__':
    main()
