#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    argv = arg[1:]
    argc = len(argv)
    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} argument:\n{:d}: {:}".format(argc, argc, argv[0]))
    else:
        print("{:d} arguments:".format(argc))
        for a in range(0, argc):
            print("{:d}: {:}".format((a + 1), argv[a]))
