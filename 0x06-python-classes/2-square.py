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
    def __init__(self, size=0):
        """ initialize the instance attributes
        Args:
            size (no type): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
