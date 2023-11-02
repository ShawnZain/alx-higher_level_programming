#!/usr/bin/python3

'''Your code should not be executed when imported - by using __import__'''
if __name__ = "__main__":

    '''import function add() from module add_0
    only use add_0 once in your code
    '''
    from add_0 import add

    '''assign value of 1 to variable a and 2 to variable b
    in 2 separate lines
    '''
    a = 1
    b = 2

    '''print <a value> + <b value> = <add(a, b) value>'''
    print("{} + {} = {}".format(a, b, add(a,b)))
