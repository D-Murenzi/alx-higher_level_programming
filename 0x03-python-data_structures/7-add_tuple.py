#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # adds two tuples
    if len(tuple_a) < 2:
        if len(tuple_a) < 1:
            a = 0
            b = 0
        else:
            a = tuple_a[0]
            b = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]
    if len(tuple_b) < 2:
        if len(tuple_b) < 1:
            c = 0
            d = 0
        else:
            c = tuple_b[0]
            d = 0
    else:
        c = tuple_b[0]
        d = tuple_b[1]
    return a+c, b+d
