#!/usr/bin/python3
"""module 10-square to create square out of Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """square class inherits form rectangle"""

    def __init__(self, size):
        """Initializes an instance

        Args:
            - size: squre length
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ function to calculate the area of a square"""
        return (self.__size ** 2)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
