#!/usr/bin/python3
"""this module to read from a UTF8 decoded file and print it out"""


def read_file(filename=""):
    """function to read a whole file and print it to the stdout

        Args:
            filename (str): the file to read from
    """

    with open(filename, 'r', encoding='utf-8') as my_file:
        for line in my_file:
            print(line, end='')
