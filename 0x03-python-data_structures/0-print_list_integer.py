#!/usr/bin/python3
def print_list_integer(my_list=[]):
    L = len(my_list)
    for i in range(L):
        print("{:d}".format(my_list[i]))
