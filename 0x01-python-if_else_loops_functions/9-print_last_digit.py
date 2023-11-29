#!/usr/bin/python3
def print_last_digit(number):
    # prints a last digit of a number
    if isinstance(number, int):
        a = str(number)
        print(a[-1], end="")
        return int(a[-1])
    else:
        return
    
