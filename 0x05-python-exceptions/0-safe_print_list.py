#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for t in range(x):
            print("{}".format(my_list[t], end="")
        print()
        return x
    except IndexError as ie:
        break
    print()
    return t
