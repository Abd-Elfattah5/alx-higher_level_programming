#!/usr/bin/python3
"""module to serialize an object with json"""


import json
"""json model to encode and decode data"""


def to_json_string(my_obj):
    """function to serialize an obj into string of json

        Args:
            my_obj (unknown): the object to deserialize

        Return:
            the string representation of an object
    """
    return (json.dumps(my_obj))
