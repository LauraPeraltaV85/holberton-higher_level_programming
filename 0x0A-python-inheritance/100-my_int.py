#!/usr/bin/python3
class MyInt(int):
    """class that inherits from int"""
    def __init__(self, n):
        self.n = n

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
