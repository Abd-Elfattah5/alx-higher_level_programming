#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    search = dir(hidden_4)
    for i in range(len(search)):
        if search[i][0] != '_':
            print(search[i])
