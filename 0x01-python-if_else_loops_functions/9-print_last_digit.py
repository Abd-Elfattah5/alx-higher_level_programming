#!/usr/bin/python3
def print_last_digit(number):
    remainder = abs(number) % 10
    print("{}".format(remainder), end='')
    return (remainder)
