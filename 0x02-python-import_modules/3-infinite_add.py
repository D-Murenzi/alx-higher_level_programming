#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    argv = arg[1:]
    argc = len(argv)
    a = 0
    for c in range(0, argc):
        a = a + int(argv[c])
    print(a)
