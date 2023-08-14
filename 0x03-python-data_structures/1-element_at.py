#!/usr/bin/python3
def element_at(my_list, idx):
    L = len(my_list)
    if idx < 0 or idx >= L:
        return (None)
    return (my_list[idx])
