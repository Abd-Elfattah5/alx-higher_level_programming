#!/usr/bin/python3

def lookup(obj):
    """ function to return all the object attributes

        Args:
            obj (unknown): some object to retreive its attributes

        Return:
            dictionary: all the object attributes
    """
    return (obj.__dict__)
