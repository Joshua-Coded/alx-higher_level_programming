#!/usr/bin/python3

import json
"""saving into json file"""

def save_to_json_file(my_obj, filename):
    """function for saving using dump"""
    with open("filename", "w") as f:
        json.dump(my_obj, f)
