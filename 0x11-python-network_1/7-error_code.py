#!/usr/bin/python3
"""This module uses  the requests package to fetch resources from
a url read from the terminal, prints the response body and if HTTPError
occurs print the error code for code that is >= 400
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    try:
        with requests.get(url) as resp:
            code = resp.status_code
            if code >= 400:
                print("Error code: {}".format(code))
            else:
                print(resp.text)
    except requests.HTTPError as e:
        code = e.code
        if code >= 400:
            print("Error code: {}".format(code))
