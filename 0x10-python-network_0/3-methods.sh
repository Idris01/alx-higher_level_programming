#!/bin/bash
# Prints the allwed request methods to a url
curl -sI "$1" | grep -i allow | cut -d ":" -f 2
