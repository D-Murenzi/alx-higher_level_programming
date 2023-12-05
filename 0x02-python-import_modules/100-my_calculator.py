#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    argv1 = sys.argv
    argv = argv1[1:]
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[1] == '+':
        print("{:d}".format(calculator_1.add(int(argv[0]), int(argv[2]))))
    elif argv[1] == '-':
        print("{:d}".format(calculator_1.sub(int(argv[0]), int(argv[2]))))
    elif argv[1] == '*':
        print("{:d}".format(calculator_1.mul(int(argv[0]), int(argv[2]))))
    elif argv[1] == '/':
        print("{:d}".format(calculator_1.div(int(argv[0]), int(argv[2]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
