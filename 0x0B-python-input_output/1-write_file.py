#!/usr/bin/python3
"""a module to write a text to file and overwrite the file"""


def write_file(filename="", text=""):
    """functions that overwrites a file with a text

        Args:
            filename (str): the file to overwrite
            text (str): the message to write
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        return (my_file.write(text))
