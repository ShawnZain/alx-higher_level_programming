#!/usr/bin/python3

'''
print combo of 2 digits
you cannot repeat the same digit twice to make 1 combo
you can only print the smallest possible combo eg print 89 and not 98
before the largest number, 89, each combo should be seprated by ", "
'''

for a in range(0, 10):
    for b in range(a + 1, 10):
        if ((a*10+b) < (b*10+a)) and ((a*10+b) != 89):
            print("{}{}".format(a, b), end=", ")
        else:
            print(89)
