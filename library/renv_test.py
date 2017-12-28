#!/usr/bin/env python
import requests
import json

DEFAULT_RANCHER_HOST = "http://localhost:8080"
API_URL = "{host}/v2-beta/projects".format(host=DEFAULT_RANCHER_HOST)

def main():
    json_data = json.loads(requests.get(API_URL).text)

    # get the project url
    project_url = json_data['data'][0]['links']['projects']

    payload = dict(
        name = "Peleu Barbos",
        description = "Just some random environment"
    )

    requests.post(API_URL, data=payload)

if __name__ == '__main__':
    main()
