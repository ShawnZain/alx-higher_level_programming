#!/usr/bin/python3

import sys


def main():
    #get the length of arguments passed
    count = len(sys.argv)

    #test if there are arguments passed
    if count == 1:
        print("0 arguments.")
    else:
        #print the number of arguments passed
        print(f"{count - 1} arguments:")

        #iterate through the arguments and print each one
        for i, arg in enumerate(sys.argv[1:], start = 1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
