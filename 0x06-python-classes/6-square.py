#!/usr/bin/python3

"""Defining square class"""


class Square:
    """Properties of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor method"""

        self.__size = size
        self.__position = position

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
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieves (gets) the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position
        Test for:
            1. value must be a tuple - isinstance(value, tuple)
            2. value must have 2 values - len(value) == 2
            3. value has to be an integer - all(isinstance(num, int) for num in value)
            4. Value has to be >= 0, raise ValueError all(num >= 0 for num in value)
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value
                

    def my_print(self):
        """Prints out the square with #s
            position[1] reprensents how many new lines before printing the square
            position[0] represents how many spaces before printing #
            The length and width of the square is 'size'
            if size == 0, print out a blank line
        """

        if self.__size == 0:
            print("")

        for new_line in range(0, self.__position[1]):
            print("")

        for length in range(0, self.__size):
            for space in range(0, self.__position[0]):
                print(" ", end = "")

            for width in range(0, self.__size):
                print("#", end = "")

            print("")
