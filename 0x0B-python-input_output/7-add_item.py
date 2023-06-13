#!/usr/bin/python3
"""This module define a script that add  arguments to a file

The arguments are first added to alist then saved to a file 'add_item.json'
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args_list = sys.argv[1:]
save_to_json_file(args_list, 'add_item.json')
