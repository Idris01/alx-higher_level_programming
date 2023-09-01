#!/usr/bin/python3
"""This module send a get request to a given url
and print the corresponding data
"""

if __name__ == "__main__":
    import urllib.request as req

    url = "https://alx-intranet.hbtn.io/status"

    with req.urlopen(url) as resp:
        data = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(
            data.decode('utf-8')))
