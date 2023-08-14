#!/usr/bin/python3
def multiple_returns(sentence):
    L = len(sentence)
    if L == 0:
        return (L, None)
    return (L, sentence[0])
