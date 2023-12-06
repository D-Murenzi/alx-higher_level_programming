#!/usr/bin/python3
def uniq_add(my_list=[]):
    # adds the unique integers in a list
    my_list.sort()
    new_list = [my_list[0]]
    for a in my_list:
        if a != new_list[-1]:
            new_list = new_list + [a]
    add = 0
    for b in new_list:
        add = add + b
    return add
