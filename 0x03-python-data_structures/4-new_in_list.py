#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # function that add new element in a list without modifying it
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        new_list = []
        new_list.extend(my_list)
        new_list[idx] = element
        return new_list
