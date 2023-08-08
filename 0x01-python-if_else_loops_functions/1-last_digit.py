#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
remain = nubmer % 10
if remain > 5:
    print(f"last digit of {number} is {remain} and is greater than 5")
elif remain < 6 and remain not 0:
    print(f"last digit of {number} is {remain} and is less than 6 and not 0")
else
print(f"last digit of {number} is {remain} and is 0")
