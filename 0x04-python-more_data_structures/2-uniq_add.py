#!/usr/bin/python3
def uniq_add(my_list=[]):
    # adds the unique integers in a list
    my_list.sort()
    new_list = set(my_list)
    add = 0
    for b in new_list:
        add = add + b
    return add
