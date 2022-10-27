#!/usr/bin/python3

"""Define a JSON-to-get function """


def from_json_string(my_str):
    """Return the python object representation of JSON string."""
    return json.loads(my_str)
