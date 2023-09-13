#!/usr/bin/python3
"""a module to write a text to file and and the text to it"""


def append_write(filename="", text=""):
    """functions that append a text to a file

        Args:
            filename (str): the file to append to
            text (str): the message to be appended
    """
    with open(filename, 'a', encoding='utf-8') as my_file:
        return (my_file.write(text))
