#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
b = str(number)
c = b[len(b) - 1]
if number < 0:
    c = -int(c)
else:
    c = int(c)
    
if c > 5:
    print(f"Last digit of {number} is {c} and is greater than 5")
elif c == 0:
    print(f"Last digit of {number} is {c} and is 0")
else:
    print(f"Last digit of {number} is {c} and is less than 6 and not 0")
