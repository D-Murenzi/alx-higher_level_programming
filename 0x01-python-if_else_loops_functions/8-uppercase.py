#!/usr/bin/python3
def uppercase(str):
    # function that capitalizes a string
    str1 = ""
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            # converts a small letters to capital
            str1 = str1 + chr(ord(a)-32)
        else:
            # prints any other letter as it is
            str1 = str1 + a
    print("{:}".format(str1))
