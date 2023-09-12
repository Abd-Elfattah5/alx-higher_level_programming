#!/usr/bin/python3
"""this module for myList to inherit from List class"""


class MyList(list):
    """this is a class to inherite from the list class"""
    def print_sorted(self):
        """ a function to print MyList sorted"""
        my_list = self[:]
        my_list.sort()
        print(my_list)
