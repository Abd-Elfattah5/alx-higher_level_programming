#!/usr/bin/python3
"""this module to return the dictionary of an object"""


def class_to_json(obj):
    """function to return the dictionary of an object

        Args:
            obj (unknown): the obj to return its dictionary
        Return:
            the dictionary of an obj
    """
    return (obj.__dict__)
