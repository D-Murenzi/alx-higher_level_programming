#!/usr/bin/python3
"""this module contains a class for square with a private a ttribute."""


class Square:
    """this class contains only size attribute which is private."""

    def __init__(self, size=0):
        """Initialize every object of the class square.

        Args:
             size: the value for size of squares side.
        """
        self.__size = size
