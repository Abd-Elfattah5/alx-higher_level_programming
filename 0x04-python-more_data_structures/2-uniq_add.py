#!/usr/bin/python3
def uniq_add(my_list=[]):
    numbers = set(my_list)
    result = 0
    for i in numbers:
        result += i
    return (result)
