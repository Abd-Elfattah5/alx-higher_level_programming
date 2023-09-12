#!/usr/bin/python3
"""module 2-is_same_class"""


def is_same_class(obj, a_class):
    """function to check if the object is the exact class type
        Args:
            - obj (unkown): the object
            - a_class (unkown): the class
        Return:
            true if it's the same or false otherwise
    """
    return True if type(obj) is a_class else False
