#!/usr/bin/python3
"""This module define a python script that displays the github id
given the password and username of a user
"""

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer {}".format(password),
            "X-GitHub-Api-version": "2022-11-28"
            }
    url = "https://api.github.com/user"
    with requests.get(url, headers=headers) as resp:
        print(resp.json().get('id', None))
