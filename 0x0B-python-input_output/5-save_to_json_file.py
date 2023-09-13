#!/usr/bin/python3
"""module to write an object with json into a file"""


import json
"""json model to encode and decode data"""


def save_to_json_file(my_obj, filename):
    """function to write a stringfied object into a file by json

        Args:
            my_obj (unknown): the object to serialize

            filename (str): the file to write to
    """
    with open(filename, 'a') as my_file:
        json.dump(my_obj, my_file)
