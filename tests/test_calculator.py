import pytest
from decimal import Decimal
from calculator.calculator import Calculator
from calculator.calculations import Calculations

@pytest.mark.parametrize("a, b, expected", [
    (Decimal(2), Decimal(3), Decimal(5)),
    (Decimal(-1), Decimal(5), Decimal(4)),
    (Decimal(0), Decimal(0), Decimal(0))
])
def test_add(a,b,expected):
    assert Calculator.add(a,b) == expected

@pytest.mark.parametrize("a,b,expected",[
    (Decimal(5), Decimal(3), Decimal(2)),
    (Decimal(10), Decimal(4), Decimal(6)),
    (Decimal(-2), Decimal(-2), Decimal(0))
])

def test_subtract(a,b,expected):
    assert Calculator.subtract(a,b) == expected

@pytest.mark.parametrize("a,b,expected",[
    (Decimal(9), Decimal(3), Decimal(3)),
    (Decimal(5), Decimal(2.5), Decimal(2)),
    (Decimal(-12), Decimal(4), Decimal(-10))
])

def test_multiply(a,b,expected):
    assert Calculator.multiply(a,b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (Decimal(9), Decimal(3), Decimal(3)),
    (Decimal(5), Decimal(2), Decimal(2.5)),
    (Decimal(-10), Decimal(5), Decimal(-2))
])
def test_divide(a, b, expected):
    assert Calculator.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal(5), Decimal(0))