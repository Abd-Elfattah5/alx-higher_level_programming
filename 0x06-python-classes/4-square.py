#!/usr/bin/python3
"""defines a class of square"""


class Square:
    """
        Square: class to define square
        Attributes:
            size (no type or value restrictions): size of square
        Method:
            __init__: initializing the class attributes
            area: function to return the square area
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

    @property
    def size(self):
        """ a size getter
            Return (type: int): the size of the instance
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ a size setter
        Args:
            value (type: int): size of the square to be set to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ calculating square area
            Return (type: int): the area of the square"""
        return (self.__size ** 2)
