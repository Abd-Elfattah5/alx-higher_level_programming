#!/usr/bin/python3
"""this is a square module definition"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """object initialization function

            Args:
                size (int): the length of the square
                x (int): the x coordinate
                y (int): the y coordinate
                id (int): the number of the object
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter property"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """function to return the printable string of the class"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.size))

    def update(self, *args, **kwargs):
        """function to update the squares values

            Args:
                args (int): the new values for each attribute
                kwargs (str, int): the new values for some attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """function to return the dictionary representation of the obj"""
        return ({"id": self.id,
                 "size": self.size,
                 "x": self.x,
                 "y": self.y})
