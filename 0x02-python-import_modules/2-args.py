#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args == 0:
        print("0 arguments.".format(args))
    if args > 1:
            print("{} arguments:".format(args))
            for argc in range(1, len(sys.argv)):
                print("{}: {}".format(argc, sys.argv[argc]))
    elif args == 1:
            print("1 argument:")
            print("{}: {}".format(args, sys.argv[1]))
