#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # replaces element in my list with new element
    new_list = []
    for a in range(len(my_list)):
        if my_list[a] == search:
            new_list = new_list + [replace]
        else:
            new_list = new_list + [my_list[a]]
    return new_list
