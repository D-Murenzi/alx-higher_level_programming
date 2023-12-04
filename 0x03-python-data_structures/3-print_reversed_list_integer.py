#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # this function prints the elements of a list in reverse
    my_list.reverse()
    for a in my_list:
        b = "{:d}".format(a)
        print(b)
