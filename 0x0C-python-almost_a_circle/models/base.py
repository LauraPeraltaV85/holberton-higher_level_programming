#!/usr/bin/python3
"""
Class base
"""

import json
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes variables assingning values
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that returns the JSON
        representation of an object (string)
        """
        if type(list_dictionaries) is list:
            if list_dictionaries is None or list_dictionaries is []:
                return "[]"
            string = json.dumps(list_dictionaries)
            return string

    @classmethod
    def save_to_file(cls, list_objs):
        """function that writes an Object to a
        text file, using a JSON representation
        """
        fn = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(fn, "w", encoding='utf-8') as fl:
            fl.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """function that returns an object
        (Python data structure) represented
        by a JSON string"""
        if json_string is None or json_string is []:
            return "[]"
        else:
            obj = json.loads(json_string)
            return obj

    @classmethod
    def create(cls, **dictionary):
        """function dummy"""
        if cls.__name__ is "Rectangle":
            n = cls(1, 5, 6, 3, 10)
            n.update(**dictionary)
            return n
        if cls.__name__ is "Square":
            s = cls(1)
            s.update(**dictionary)
            return n

    @classmethod
    def load_from_file(cls):
        """function to load from json"""
        fn = cls.__name__ + ".json"
        n = 0
        if not fn:
            return "[]"
        else:
            with open(fn, 'r', encoding="utf-8") as f:
                x = [cls.create(**n) for n in cls.from_json_string(f.read())]
                return x
