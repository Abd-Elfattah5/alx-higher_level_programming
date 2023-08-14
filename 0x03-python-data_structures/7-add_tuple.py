#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    L1 = len(tuple_a)
    L2 = len(tuple_b)

    if L1 < 2:
        if L1 == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if L2 < 2:
        if L2 == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return ((tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))
