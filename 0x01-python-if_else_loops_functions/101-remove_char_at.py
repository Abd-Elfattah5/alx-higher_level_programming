#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ""
    for i in range(len(str)):
        if i == n:
            continue
        temp += str[i]
    return (temp)
