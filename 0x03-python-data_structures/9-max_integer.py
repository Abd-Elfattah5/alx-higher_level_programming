#!/usr/bin/python3
def max_integer(my_list=[]):
    L = len(my_list)
    if L == 0:
        return None
    max_int = -1e8
    for i in range(L):
        if my_list[i] > max_int:
            max_int = my_list[i]
    return max_int
