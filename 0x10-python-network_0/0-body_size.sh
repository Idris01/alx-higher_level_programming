#!/bin/bash
# Prints the body size of a get request to a url
curl -sI "$1" | grep -i content-length | cut -d " " -f 2
