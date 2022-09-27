#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file:
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argv = sys.argv
filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []
args = argv[1:]
for i in args:
    my_list.append(i)
save_to_json_file(my_list, filename)
