#!/usr/bin/python3


def print_last_digit(number):

    if number < 0:
        print("{}".format(abs(number) % 10), end="")
        return (abs(number) % 10)
    elif number == 0:
        print("{}".format(number), end="")
    else:
        print("{}".format(number % 10), end="")
        return (number % 10)
