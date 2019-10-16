#!/usr/bin/python3
def number_of_lines(filename=""):
    """returns number of lines"""
    with open(filename) as fl:
        linum = 0

        while True:
            line = fl.readline()
            if not line:
                break
            linum += 1
        return linum
