#!/usr/bin/python3
"""this module is for base class creation"""

import json
import turtle
import csv


class Base:
    """Base class for shapes

        Attributes:
                __nb_objects (int): number of objects taken from this class

        methods:
            __init__: the initialization method of the object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization function

                Args:
                    id (int): the id of the class objects
                Return: nothing
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function to return the json string representation of an object

            Args:
            list_dictionaries (dict): the dictionaires list to be turned
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function to turn a list of objects into json strings
            and save them to a file

            Args:
                cls (cls): the class type of the list of objects
                list_objs (cls): the list of objects
        """
        name = cls.__name__ + ".json"
        with open(name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """function to return the list of dictionaries
        represented by the json string

            Args:
                json_string (str): the string representing the list
            Return: the list of dictionaries
        """
        if json_string is None or json_string == "[]":
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """function to return an obj of a class initialized with known values

            Args:
                cls (cls): the class type
                dictionary (dict): a dictionary of the obj values
            Return: the new obj with updated values
        """
        if dictionary and dictionary != {}:
            print("class_name = {}".format(cls.__name__))
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            else:
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """function to return list of objects created from json string
        obtained from file

            Return: a list of objects of emptylist
        """

        name = str(cls.__name__) + ".json"
        try:
            with open(name, "r") as my_file:
                list_dict = Base.from_json_string(my_file.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """function to write to a csv file

            Args:
                list_objs (list of cls): a list containig the objs to save
        """
        name = cls.__name__ + ".csv"
        with open(name, "w", newline="") as my_file:
            if list_objs is None or len(list_objs) == 0:
                my_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]

                writer = csv.DictWriter(my_file, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """function to read from a csv file

            Args:
                cls (cls): the class of list should be returned
            Return: a list of objects from the csv file
        """
        name = cls.__name__ + ".csv"

        with open(name, "r", newline="") as my_file:
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]
            string_readed = csv.DictReader(my_file, fieldnames=fields)
            list_dicts = [dict([k, int(v)] for k, v in d.items())
                          for d in string_readed]
            return [cls.create(**d) for d in list_dicts]
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """function to draw all the rectangles and the squares
            in a split window

            Args:
                list_rectangles (Rectangle): the rectangles list to draw
                list_squares (Square): the squares list to draw
        """
        curser = turtle.Turtle()

        for rect in list_rectangles:
            curser.penup()
            curser.goto(rect.x, rect.y)
            curser.pendown()
            curser.forward(rect.width)
            curser.left(90)
            curser.forward(rect.height)
            curser.left(90)
            curser.forward(rect.width)
            curser.left(90)
            curser.forward(rect.height)

        for sqr in list_squares:
            curser.penup()
            curser.goto(sqr.x, sqr.y)
            curser.pendown()
            for edge in range(4):
                curser.forward(sqr.size)
                curser.left(90)
        turtle.end()
