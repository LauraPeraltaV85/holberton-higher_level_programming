#!/usr/bin/python3
def write_file(filename="", text=""):
    """writes file"""
    with open(filename, mode="w", encoding="utf-8") as fl:
        lines = fl.write(text)
        return lines
