#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
remain = abs(number) % 10
if number < 0:
    remain = remain * -1
if remain > 5:
    print("last digit of {} is {} and\
 is greater than 5".format(number, remain))
elif remain < 6 and remain != 0:
    print("last digit of {} is {} and\
 is less than 6 and not 0".format(number, remain))
else:
    print("last digit of {} is {} and is 0".format(number, remain))
