#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # deletes a key in dictionary
    if key:
        del a_dictionary[key]
