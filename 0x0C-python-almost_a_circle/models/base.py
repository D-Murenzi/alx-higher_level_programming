#!/user/bin/python3
"""
This module contains the base class of all other classes created in
this project.
"""


class Base:

    """ Keep track of all instances created to prevent the duplication of
    an object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the instances of this class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = _nb_objects
