#!/usr/bin/python3
"""module to create pascal triangle"""


def pascal_triangle(n):
    """function to create pascal triangle

        Args:
            n (int): number of rows in the triangle
        Return:
            list of row lists
    """
    if (n) < 1:
        return []
    my_list = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        my_list.append(row)
    return (my_list)
