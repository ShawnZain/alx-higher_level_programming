#!/usr/bin/python3

'''Import functions from file calculator_1.py
Do not use '*' or '__import__'
Use module name only once in the program
Program shoudl not execute when its not main
'''
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    '''define variables each in own line'''
    a = 10
    b = 5

    '''call each of the imported functions'''
    '''add'''
    print("{} + {} = {}".format(a, b, add(a, b)))

    '''sub'''
    print("{} - {} = {}".format(a, b, sub(a, b)))

    '''mul'''
    print("{} * {} = {}".format(a, b, mul(a, b)))

    '''div'''
    print("{} / {} = {}".format(a, b, div(a, b)))
