#!/usr/bin/python3


def pow(a, b):

    #check if a is negative
    if a < 0:
        return("{:d}".format(-1 * (abs(a) ** b)))
    elif b < 0:
        return("{:f}".format(1 / (a ** abs(b))))
    else:
        return("{:d}".format(a ** b))
