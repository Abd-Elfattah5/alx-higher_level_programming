#!/usr/bin/python3
"""module to read an object with json from a file"""


import json
"""json model to encode and decode data"""


def load_from_json_file(filename):
    """function to retrieve a stringfied object from a file by json
    and return it to its form

        Args:
            filename (str): the file to write to

        Return: the object
    """
    with open(filename, 'r') as my_file:
        return (json.load(my_file))
