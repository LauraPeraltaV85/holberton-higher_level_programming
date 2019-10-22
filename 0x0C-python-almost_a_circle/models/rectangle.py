#!/usr/bin/python3
"""
Class rectangle
"""


from models.base import Base


class Rectangle(Base):
    """defines rectangle, inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """validation"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """validation"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """validation"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """validation"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
        return self.__y

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays square #"""
        for c in range(self.y):
            print()
        for count in range(self.height):
            for i in range(self.x):
                print(" ", end='')
            for count in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """returns string"""
        arg_list = [self.id, self.x, self.y, self.width, self.height]
        return "[Rectangle] ({}) {}/{} - {}/{}".format(*arg_list)

    def update(self, *args, **kwargs):
        """uses args and kwargs"""
        a = ['id', 'width', 'height', 'x', 'y']
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
        w = self.width
        h = self.height
        r = {"id": i, "width": w, "height": h, "x": self.x, "y": self.y}
        return r
