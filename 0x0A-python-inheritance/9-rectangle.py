#!/usr/bin/python3
"""module 8-rectangle to create rectangle out of BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits form BaseGeometry"""

    def __init__(self, width, height):
        """Initializes an instance

        Args:
            - width: rectangle width
            - height: rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
