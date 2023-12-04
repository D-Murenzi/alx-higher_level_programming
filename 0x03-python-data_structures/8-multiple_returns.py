#!/usr/bin/python3
def multiple_returns(sentence):
    ''' this function returns a tuple of length of string and its
    character'''
    if len(sentence) == 0:
        a = 0
        b = None
    else:
        a = len(sentence)
        b = sentence[0]
    return a, b
