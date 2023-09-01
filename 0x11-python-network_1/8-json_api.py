#!/usr/bin/python3
"""This module define a script that send a post request and process
the json response
"""

if __name__ == '__main__':
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {'q': q}
    with requests.post(url, data) as resp:
        try:
            json_data = resp.json()
            if json_data:
                print("[{}] {}".format(
                    json_data.get('id'),
                    json_data.get('name')))
            else:
                print("No result")
        except Exception:
            print("Not a valid JSON")
