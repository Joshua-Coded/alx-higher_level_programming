#!/usr/bin/python3


"""saving a json file function"""
import json

def save_to_json_file(my_obj, filename):

    """the function"""

    with open("filename", "w") as f:
        json.dump(my_obj, f)
