#!/usr/bin/python3
class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
            self.__width = width
            self.__height = height
            Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

    @property
    def heigth(self):
        return self.__height

    @heigth.setter
    def height(self, value):
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """prints rectangle of hashtags"""
        hash_str = ""
        if self.__width == 0 or self.__height == 0:
            return hash_str
        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)
        for count in range(self.__height):
            for count2 in range(self.__width):
                hash_str += self.print_symbol
            if (count < self.__height - 1):
                hash_str += "\n"
        return hash_str


    def __repr__(self):
        """returns a representation string of the rectangle"""
        return "Rectangle(%s, %s)" % (self.__width, self.__height)

    def __del__(self):
        """prints message when object deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
