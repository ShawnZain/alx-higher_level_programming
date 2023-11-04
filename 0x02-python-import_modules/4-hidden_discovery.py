#!/usr/bin/python3

import hidden_4


def main():
    """Get the names that are in the file using the dir() function.
    Go through each name to make sure that only the ones
    that do not start with '__' are stored in the names list.
    Print each name from the sorted list of names.
    Sorting will be handled with the sorted() method
    """

    names = [name for name in dir(hidden_4) if not name.startswith('__')]

    for name in sorted(names):
        print(name)


if __name__ == "__main__":
    main()
