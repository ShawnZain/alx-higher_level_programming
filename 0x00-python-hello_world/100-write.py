#!/usr/bin/python3

import sys


def main():
    #write a message to the standarr error
    sys.stderr.write("and that piece of art is useful"
            + " - Dora Korpar, 2015-10-19\n")

    #exit with a status of 1
    sys.exit(1)


if __name__ == "__main__":
    main()
