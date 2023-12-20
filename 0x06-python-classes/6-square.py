#!/usr/bin/python3
"""This module defines a class square with private attribute.

the attribute can be instantialized but under conditions.
"""


class Square:
    """This class is square class.

    it has private size that is initialized under conditions.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize size to  size value after checcking condition.

        Args:
            size(int): an integer value for size of square.
            position(touple): coardinates of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the position of the square.

        the getter checks if position is a touple and raises an error
        if its not. if it is it assigns the value to position.
        """
        return self.__position

    @position.setter
    def position(self, position=(0, 0)):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for a in position:
                if not isinstance(a, int):
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
                self.__position = position

    def area(self):
        """Return area of a square."""
        return (self.size * self.size)

    def my_print(self):
        """Print area on stduot."""
        if self.size == 0:
            print()
        else:
            for a in range(self.size):
                if self.position[1] > 0:
                    print("_"*self.position[0]+"#"*self.size+'\n')
                else:
                    print("_"*self.position[0]+"#"*self.size)
