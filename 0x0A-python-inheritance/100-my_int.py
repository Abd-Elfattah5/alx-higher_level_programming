#!/usr/bin/python3
"""module 100-my_int to revert the operations"""


class MyInt(int):
    """class MyInt is rebel"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
