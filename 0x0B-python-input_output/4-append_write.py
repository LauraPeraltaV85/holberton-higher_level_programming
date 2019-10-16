#!/usr/bin/python3
def append_write(filename="", text=""):
        """appends line at the end of file"""
        with open(filename, mode="a", encoding="utf-8") as fl:
            return fl.write(text)
