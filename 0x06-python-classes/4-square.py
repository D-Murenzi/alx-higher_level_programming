#!/usr/bin/python3
"""This module defines a class square with private attribute.

the attribute can be instantialized but under conditions.
"""


class Square:
    """This class is square class.

    it has private size that is initialized under conditions.
    """

    def __init__(self, size=0):
        """Initialize size to  size value after checcking condition.

        Args:
            size(int): an integer value for size of square.
        """
        self.size = size

    @property
    def size(self):
        """:obj:square size.

        the getter checks for conditions and may raise errors
        depenging on conditions. Errors include value error is size is
        less than 0 and TypeError is it not an integer.
        """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return area of a square."""
        return (self.size * self.size)
