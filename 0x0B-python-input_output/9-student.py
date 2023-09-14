#!/usr/bin/pytnon3
"""class module for a student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """function to initialize the obj values

            Args:
                self: obj self
                first_name (str): students name
                last_name (str): students last name
                age (int): students age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function to return the attributes of the object"""

        return (self.__dict__)
