#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    #function that prints x elts of list if they are integers
    b = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
            b = b + 1
        except TypeError:
            continue
        except ValueError:
            continue
        except IndexError:
            return b
    print()
    return b
