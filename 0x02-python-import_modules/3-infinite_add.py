#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for argc in range(1, len(sys.argv)):
        result = result + int(sys.argv[argc])
    print("{}".format(result))
