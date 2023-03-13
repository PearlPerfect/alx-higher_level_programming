#!/usr/bin/python3
if _name_ == "_main_":
    import sys
    args = len(sys.argv)
    print("{} ".format(args - 1), end="")
    if args == 1:
        print("arguments.")
    elif args > 1:
        if args == 2:
            print("argument:")
        elif args > 2:
            print("arguments:")
        for i in range(args - 1):
            print("{}: {}".format((i + 1), sys.argv[i + 1]))
