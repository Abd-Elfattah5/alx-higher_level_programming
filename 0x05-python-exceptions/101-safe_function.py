#!/usr/bin/python3


import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except (TypeError, ValueError, ZeroDivisionError, IndexError):
        sys.stderr.write("Exception: {}\n".format(sys.exc_info()[1]))
        return (None)
