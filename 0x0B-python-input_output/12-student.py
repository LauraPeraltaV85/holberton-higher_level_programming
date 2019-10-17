#!/usr/bin/python3
"""
class student
"""


class Student:
    """class that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            d = {}
            for e in attrs:
                if e in self.__dict__:
                    d[e] = self.__dict__[e]
            return d
        else:
            i = vars(self)
            return i
