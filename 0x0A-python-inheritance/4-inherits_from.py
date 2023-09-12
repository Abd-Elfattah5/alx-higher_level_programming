#!/usr/bin/python3
""" module 4-inherits_from to check the inheritance"""


def inherits_from(obj, a_class):
    """function to check if an object iherits from a class

        Args:
            - obj(unknown): the object
            - a_class(unkown): the class
        Return:
            True if inherits and False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
