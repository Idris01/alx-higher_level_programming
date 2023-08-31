#!/bin/bash
# load post data for a request from json file
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1" 
