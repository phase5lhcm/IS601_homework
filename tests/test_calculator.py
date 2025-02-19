import pytest
from decimal import Decimal
from faker import Faker
from calculator.calculator import Calculator
from calculator.operations import add, subtract, multiply, divide

faker = Faker()

@pytest.mark.parametrize("a, b, expected", [
    (Decimal(faker.random_int(min=-100, max=100)), Decimal(faker.random_int(min=-100, max=100))) for _ in range(5)
])
def test_add(a,b):
    expected = a + b
    assert Calculator.add(a,b) == expected

@pytest.mark.parametrize("a,b,expected",[
 (Decimal(faker.random_int(min=-100, max=100)), Decimal(faker.random_int(min=-100, max=100))) for _ in range(5)
])

def test_subtract(a,b):
    expected = a - b
    assert Calculator.subtract(a,b) == expected

@pytest.mark.parametrize("a,b,expected",[
    (Decimal(faker.random_int(min=-20, max=20)), Decimal(faker.random_int(min=-20, max=20))) for _ in range(5)
])

def test_multiply(a,b):
    expected = a * b
    assert Calculator.multiply(a,b) == expected

@pytest.mark.parametrize("a, b, expected", [
 (Decimal(faker.random_int(min=-100, max=100)), Decimal(faker.random_int(min=-100, max=100))) for _ in range(5)
])
def test_divide(a, b):
    expected = a / b
    assert Calculator.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal(faker.random_int(min=1, max=100)), Decimal(0))
