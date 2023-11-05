#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def main():
    """A simple calculator.
    Takes 3 arguments only:

    sys.argv[1]: number
    sys.argv[2]: operator
    sys.argv[3]: number

    performs the operation and prints it
    """

    arg_len = len(sys.argv)
    result = 0
    a = None #first number
    b = None #second number
    op = None #operand

    #error if arguments passed are not 3
    if arg_len != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    
    #checking the operator that has been passed
    if op == "+":
        result = add(a, b)
        print(f"{a} + {b} = {result}")
        return
    elif op == "-":
        result = sub(a, b)
        print(f"{a} - {b} = {result}")
        return
    elif op == "*":
        result = mul(a, b)
        print(f"{a} * {b} = {result}")
        return
    elif op == "/":
        result = div(a, b)
        print(f"{a} / {b} = {result}")
        return
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    #don't run main when its imported
    main()
