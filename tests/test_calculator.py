import pytest
from decimal import Decimal
from calculator.calculator import Calculator
from calculator.calculations import Calculations

@pytest.fixture
def clear_history():
    """Fixture to clear calculation history before each test."""
    Calculations.clear_history()

def test_add(clear_history):
    assert Calculator.add(Decimal(3), Decimal(2)) == Decimal(5)

def test_subtract(clear_history):
    assert Calculator.subtract(Decimal(5), Decimal(2)) == Decimal(3)

def test_multiply(clear_history):
    assert Calculator.multiply(Decimal(4), Decimal(3)) == Decimal(12)

def test_divide(clear_history):
    assert Calculator.divide(Decimal(8), Decimal(2)) == Decimal(4)

def test_divide_by_zero(clear_history):
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal(5), Decimal(0))

def test_calculation_history(clear_history):
    Calculator.add(Decimal(1), Decimal(1))
    assert len(Calculations.get_history()) == 1
    assert Calculations.get_latest().perform() == Decimal(2)
