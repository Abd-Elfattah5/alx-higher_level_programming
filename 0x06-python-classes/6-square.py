#!/usr/bin/python3
"""defines a class of square"""


class Square:
    """
        Square: class to define square
        Attributes:
            size (type: int): size of square
            position (type: tuple of int): coordinates
        Method:
            __init__: initializing the class attributes
    """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize the instance attributes
        Args:
            size (type: int): size of the square
            position (type: tuple of int): coordinates
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ getter function to the position
            Return (type: tupe of int): positoin
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter function to set the square position
            Args:
                value(type: tuple of int): the position of the square
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(selaf):
        """ calculating square area
            Return (type: int): the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """ fucntion to print the square
        """
        if (self.__size == 0):
            print()
        else:
            temp1 = self.__position[0]
            temp2 = self.__position[1]

            for i in range(temp2):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * temp1, "#" * self.__size))
