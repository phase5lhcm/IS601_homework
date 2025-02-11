"""Defines basic math operations """
from decimal import Decimal


def add(a: Decimal, b: Decimal) -> Decimal:
    """Use to perform the sum of two numbers """
    return a + b


def subtract(a: Decimal, b: Decimal) -> Decimal:
    """ Use to perform the subtraction of two numbers """
    return a - b


def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Use to multiply return the product of two numbers"""
    return a * b


def divide(a: Decimal, b: Decimal) -> Decimal:
    """Use to return the quotient of two numbers """
    if b == 0:
        raise ZeroDivisionError("Cannot perform operation")
    return a / b
