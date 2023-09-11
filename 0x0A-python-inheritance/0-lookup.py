#!/usr/bin/python3
"""this a lookup module """


def lookup(obj):
    """ function to return all the object attributes

        Args:
           - obj (unknown): some object to retreive its attributes

        Return:
            dictionary: all the object attributes
    """
    return dir(obj)
