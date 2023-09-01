#!/usr/bin/python3
"""This module takes a url and send a get request then print the
response body while handling possilbe HTTPErrors
"""

if __name__ == "__main__":
    import urllib.request as req
    import urllib.parse as parse
    from urllib.error import HTTPError
    import sys

    url = sys.argv[1]

    try:
        with req.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
