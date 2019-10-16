#!/usr/bin/python3
def from_json_string(my_str):
    """function that returns an object
    (Python data structure) represented
    by a JSON string"""
    import json
    obj = json.loads(my_str)
    return obj
