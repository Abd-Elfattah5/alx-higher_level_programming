def replace_in_list(my_list, idx, element):
    L = len(my_list)
    if idx >= 0 and idx < L:
        my_list[idx] = element
    return (my_list)
