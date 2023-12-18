#!/usr/bin/python3
def safe_print_integer(value):
    # this funciton prints a value if it integer
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
