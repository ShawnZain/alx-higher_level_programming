#!/usr/bin/python3

"""Defining square class"""


class Square:
    """Properties of a square"""

    def __init__(self, size=0):
        """Constructor method

        Size should be of type int
        >>>a_square = Square('O')
        Traceback (most recent call last):
        ...
        TypeError: 'size must be an integer'

        Size should always be greater than 0
        >>>b_square = Square(-1)
        Traceback (most recent call last):
        ...
        ValueError: 'size must be >= 0'

        Correct initlialization of the instance
        >>>c_square = Square(2)

        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """The area of a square

        All tests shall pass as correct input is expected
        >>>new_square = Square(2)
        >>>print(new_square.area())
        4

        >>>new_square = Square(9)
        >>>print(new_square.area())
        81

        """

        return (self.__size * self.__size)

    @property
    def size(self):
        """Retrieves (gets) the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a new value for size
        The new value for size should meet the same criteria as when initializing it:
            It must be an integer
            Size should always be greater than 0

        Correct initlialization of the instance
        >>>c_square = Square(2)

        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value
