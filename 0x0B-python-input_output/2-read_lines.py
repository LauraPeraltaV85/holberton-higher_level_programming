#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """reads n lines on file"""
    with open(filename, encoding="utf-8") as fl:
        if nb_lines <= 0:
            print(fl.read(), end="")
        for e in range(nb_lines):
            print(fl.readline(), end="")
