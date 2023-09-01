#!/usr/bin/python3
"""This Module define a script that takes a url
and print the correspondin 'X-Request-Id' value
"""

if __name__ == "__main__":
    import sys
    import urllib.request as req

    url = sys.argv[1]
    with req.urlopen(url) as resp:
        print(resp.headers["X-Request-Id"])
