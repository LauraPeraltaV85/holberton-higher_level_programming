#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines square, inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """prints string with id, coordinates, and size"""
        arg = [self.id, self.x, self.y, self.size]
        return "[Square] ({}) {}/{} - {}".format(*arg)

    def update(self, *args, **kwargs):
        a = ['id', 'size', 'x', 'y']
        count = 0
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
                count += 1
        else:
            for c in args:
                setattr(self, a[count], c)
                count += 1

    def to_dictionary(self):
        o = vars(self)
        return o
