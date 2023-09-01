#!/usr/bin/python3
"""This module takse a url and an email, then
send a post request to the url with the email
"""

if __name__ == "__main__":
    import urllib.request as req
    import urllib.parse as parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode(
            {'email': email}).encode('utf-8')
    post_request = req.Request(url, data)

    with req.urlopen(post_request) as resp:
        print(resp.read().decode('utf-8'))
