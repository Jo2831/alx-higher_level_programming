#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle
        Args:
            width (int): the width of new rectangle.
            height (int): the height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """get the hight of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if isinstance(height, int):
            if height < 0:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')
        self.__height = height

    """
    Calculate area of Rectangle.
    """
    def area(self):
        return self.__height * self.__width

    """
    Calculate perimeter of Rectangle object.
    """
    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2
