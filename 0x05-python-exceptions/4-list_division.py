#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # function that adds elements of a list
    try:
        new_list = []
        for a in range(list_length):
            try:
                divident = my_list_1[a] / my_list_2[a]
                new_list.append(divident)
            except TypeError:
                divident = 0
                new_list.append(divident)
                print("wrong type")
            except ValueError:
                divident = 0
                new_list.append(divident)
            except ZeroDivisionError:
                divident = 0
                new_list.append(divident)
                print("division by 0")
            except IndexError:
                divident = 0
                new_list.append(divident)
                print("out of range")
    finally:
        return new_list
