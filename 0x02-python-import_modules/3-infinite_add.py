#!/usr/bin/python3

import sys


def main():
    """A program that adds all the arguments passed to it
    First check how many arguments have been passed.
    If non, print 0
    Otherwise, iterate through it, cast the arguments to int
    and get their sum, until the end.
    Print the sum only
    """

    sum = 0

    arg_count = len(sys.argv)
    if arg_count == 1:
        print(f"{sum}")

    else:
        for i, arg in enumerate(sys.argv[1:]):
            sum += int(arg)

    print(f"{sum}")


if __name__ == "__main__":
    main()
