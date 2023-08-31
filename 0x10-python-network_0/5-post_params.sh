#!/bin/bash
# send a POST request with data  to a url
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
