#!/usr/bin/python3
"""Create a Rectangle class."""


class Rectangle:
    """Retangle object with getter and setters
    """
    def __init__(self, width=0, height=0):
        """initializing Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.__width * self.height

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0:
        return (self.__width + self.__height) * 2
