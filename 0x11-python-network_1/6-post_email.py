#!/usr/bin/python3
"""This module uses  the requests package to send a post request
then print the response body
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    with requests.post(url, data) as resp:
        print(resp.text)
