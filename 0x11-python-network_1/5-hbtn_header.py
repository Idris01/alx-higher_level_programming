#!/usr/bin/python3
"""This module uses  the requests package to fetch resources from
a url read from the terminal and print th value of 'X-Request-Id'
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    with requests.get(url) as resp:
        print(resp.headers.get('X-Request-Id'))
