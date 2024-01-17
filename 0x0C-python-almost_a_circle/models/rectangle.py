#!/usr/bin/python3
"""
This module contains a rectangle with its attributes.
"""

from base import Base
class rectangle(Base):
    """
    the class rectangle conatins a rectangle, four sided polygon with
    two equal sizes.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """return the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """return the height of a rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """return the value of x of a rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        if not isintance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("X must be >= 0")
        self.__x = x

    @property
    def y(self):
        """return the value of y of a rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ return the value of area of a rectangle."""
        return (self.__width * self.__height)

    def display(self):
        """print the rectangle on stdout. """
        for i in range(self.__height):
            print("#"*self.__width, file=stdout)

    def __str__(self):
        """overide __str__method."""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__id, self.__x, self.__y, self.__width, self.__height)
    
