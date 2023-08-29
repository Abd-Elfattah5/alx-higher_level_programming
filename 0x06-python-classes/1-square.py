#!/usr/bin/python3
"""defines a class of square"""


class Square:
    """
        Square: class to define square
        Attributes:
            size (no type or value restrictions): size of square
        Method:
            __init__: initializing the class attributes
    """
    def __init__(self, size):
        """ initialize the instance attributes
        Args:
            size (no type): size of the square
        """
        self.__size = size
