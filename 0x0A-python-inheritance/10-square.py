#!/usr/bin/python3
"""module 10-square to create square out of Rectangle"""


Rectangle = __import__('7-Rectangle').Rectangle


class Square(Rectangle):
    """square class inherits form rectangle"""

    def __init__(self, size):
        """Initializes an instance

        Args:
            - size: squre length
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)
