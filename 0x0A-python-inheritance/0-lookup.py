#!/usr/bin/python3
"""
Returns list of attributes and methods of an object
"""


def lookup(obj):
    """Returns list of attributes and methods of an object"""
    c = dir(obj)
    return c
