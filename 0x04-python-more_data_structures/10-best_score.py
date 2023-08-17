#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)

    key = (list(a_dictionary))[0]
    value = a_dictionary[key]

    for i in a_dictionary:
        if a_dictionary[i] > a_dictionary[key]:
            key = i
            value = a_dictionary[key]
    return (key)
