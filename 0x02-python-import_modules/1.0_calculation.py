#!/usr/bin/python3

def add(a, b):
    """takes 2 arguments a and b and gives us the sum
    tests if a and b are int or floats and if not
    return an error
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise ValueError("'a' and 'b' should be numeric")


def diff(a, b):
    """takes 2 arguments a and band gives us the difference
    tests if a and b are int or float and if not
    return error
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise ValueError("'a' and 'b' should be numeric")


def prod(a, b):
    """takes 2 arguments a and b and gives us the product
    tests if a and b are int or float and in not
    return error
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    else:
        raise ValueError("'a' and 'b' should be numeric")


def div(a, b):
    """takes 2 arguments a and b and gives us the resultof dividing
    test if a and b are int or float
    if they are tests if b == 0 as division by 0 will give error
    2 possible errors to raise
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b == 0:
            raise ZeroDivisionError("Division by zero is infinity")
        return a / b
    else:
        raise ValueError("'a' and 'b' should be numeric")


def main():
    a = input("Enter a number: ")
    b = input("Enter another number: ")

    if not a.isnumeric() or not b.isnumeric():
        print("Input should be numeric.")
        return

    a = float(a)
    b = float(b)

    try:
        print("{} + {} = {}".format(a, b, add(a, b)))
        print("{} - {} = {}".format(a, b, diff(a, b)))
        print("{} * {} = {}".format(a, b, prod(a, b)))
        print("{} / {} = {}".format(a, b, div(a, b)))
    except ValueError as e:
        print("Input validation error: ", e)
    except ZeroDivisionError as e:
        print("Zero divison error: ", e)


if __name__ == "__main__":
    main()
