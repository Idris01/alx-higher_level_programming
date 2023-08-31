#!/bin/bash
# print the status code for the request
curl -s -o /dev/null -w "%{http_code}" "$1"
