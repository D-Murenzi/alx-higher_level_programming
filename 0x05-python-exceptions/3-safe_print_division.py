#!/usr/bin/python3
def safe_print_division(a, b):
    # divides two ints
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    except (ValueError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
