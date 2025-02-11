from decimal inport decimal

"""Use to perform the sum of two numbers """
def add(a: Decimal, b:Decimal) -> Decimal:
    return a + b

""" Use to perform the subtraction of two numbers """
def subtract(a: Decimal, b:Decimal) -> Decimal:
    return a -b 

"""Use to multiply return the product of two numbers"""
def multiply(a: Decimal, b:Decimal) -> Decimal:
    return a * b

"""Use to return the quotient of two numbers """
def divide(a:Decimal, b:Decimal) -> Decimal:
    if b == 0:
        raise ZeroDivisionError("Cannot perform operation")
    return a / b

    
