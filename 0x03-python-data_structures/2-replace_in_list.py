#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # this function replaces an element at idx in my_list
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
