#!/usr/bin/python3
def uppercase(str):
    # function that capitalizes a string
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            # converts a small letters to capital
            print("{:s}".format(chr(ord(a)-32)), end="")
        else:
            # prints any other letter as it is
            print("{:}".format(a), end="")