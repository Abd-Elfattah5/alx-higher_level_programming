#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        num = 0
    else:
        num = 32
    print("{}".format(chr(i - num)), end='')
