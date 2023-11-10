#!/usr/bin/python3


def pow(a, b):

    #check if a is negative
    if a < 0:
        return("{}".format(-1 * (abs(a) ** b)))
    elif b < 0:
        return("{}".format(1 / (a ** abs(b))))
    else:
        return("{}".format(a ** b))
