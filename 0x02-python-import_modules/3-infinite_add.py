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
            try:
                sum += int(arg)
            except ValueError:
                """Handling value error when user passes
                an argument that is not a number
                """
                print(f"Invalid argument at position {i + 1},"
                        f" '{arg}' is not a valid number")
                return

    print(f"{sum}")


if __name__ == "__main__":
    main()
