#!/usr/bin/python3
"""module to deserialize an object with json"""


import json
"""json model to encode and decode data"""


def from_json_string(my_obj):
    """function to deserialize a string into object by json

        Args:
            my_obj (unknown): the object to deserialize

        Return:
            the object
    """
    return (json.loads(my_obj))
