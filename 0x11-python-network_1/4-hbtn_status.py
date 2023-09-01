#!/usr/bin/python3
"""This module uses  the requests package to fetch resources
"""

if __name__ == '__main__':
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as resp:
        data = resp.text
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
