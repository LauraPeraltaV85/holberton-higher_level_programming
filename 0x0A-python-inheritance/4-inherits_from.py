#!/usr/bin/python3
"""
Function that dertemines if object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """Function that returns True if the object
    is an instance of a class that inherited (directly
    or indirectly) from the specified class; otherwise False.
    """
    if type(obj) is a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
