#!/usr/bin/python3
""" module 3-is_kind_of_class to check if an obj is a kind of class"""


def is_kind_of_class(obj, a_class):
    """function to check if obj is kind of the class a_class

        Args:
            - obj (unkown): object
            - a_class (unkown): some class
        Return:
            True if kind of and false otherwise
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    else:
        return False
