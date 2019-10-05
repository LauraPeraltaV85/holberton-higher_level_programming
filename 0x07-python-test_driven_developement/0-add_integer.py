#!/usr/bin/python3
"""

    My calculation module

"""

def add_integer(a, b=98):
    """ Addition function """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    c = a + b
    return int(c) 
