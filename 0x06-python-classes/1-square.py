#!/usr/bin/python3
"""Module Contain: class square"""


class square:
    """
        Square: Define square
        Attributes:
            size: Size of square
        Method:
            __int__:  __init__: init of size attribute for each instance
    """
    def __init__(self, size):
        """
         Initialization of attributes for all instances
            Args:
                size (no type): size of the square
        """
        self.__size = size
