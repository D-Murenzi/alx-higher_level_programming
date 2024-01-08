#!/usr/bin/python3
"""modele contains the function that look into object dictionary."""


def lookup(obj):
    """return list of attributes of the object."""
    if obj:
        return dir(obj)
