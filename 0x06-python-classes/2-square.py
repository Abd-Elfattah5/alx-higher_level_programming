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
        if (isinstance(size, int)):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
