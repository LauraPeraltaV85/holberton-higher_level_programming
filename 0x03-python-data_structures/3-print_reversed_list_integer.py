#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for x in reversed(my_list):
        if len(my_list) == 0:
            break
        print("{:d}".format(x))
