#!/usr/bin/python3
"""
Class square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defines square, inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes attributes"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """defines size"""
        return self.size

    @size.setter
    def size(self, value):
        """assignation"""
        self.size = value
        self.height = value

    def __str__(self):
        """prints string with id, coordinates, and size"""
        arg = [self.id, self.x, self.y, self.size]
        return "[Square] ({}) {}/{} - {}".format(*arg)

    def update(self, *args, **kwargs):
        """uses args and kwargs"""
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
        """to dictionary"""
        i = self.id
        s = self.size
        r = {"id": i, "size": s, "x": self.x, "y": self.y}
        return r
