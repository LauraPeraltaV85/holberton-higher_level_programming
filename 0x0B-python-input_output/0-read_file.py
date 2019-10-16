#!/usr/bin/python3
def read_file(filename=""):
    """reads file"""
    with open(filename, encoding="UTF-8") as fl:
        read_fl = fl.read()
        print(read_fl, end="")
