#!/bin/bash
# Prints the allwed request methods to a url
curl -sI -X OPTIONS "$1" | grep Allow |sed -e s/Allow:\ //g
