#!/usr/bin/python3
""" print the first 10 most recent github commit of a user with a
given repo
"""

if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]

    headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-version": "2022-11-28"
            }
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    with requests.get(url, headers=headers) as resp:
        for count, item in enumerate(resp.json()):
            if count == 10:
                break
            print("{}: {}".format(
                item.get('sha'),
                item.get('commit').get('author').get("name")))
