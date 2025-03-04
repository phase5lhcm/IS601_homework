import pytest
from faker import Faker
from calculator.commands.add import Add
from calculator.commands.subtract import Subtract
from calculator.commands.multiply import Multiply
from calculator.commands.divide import Divide

fake = Faker()

def test_add_command():
    first_operand = fake.random_int(min=0, max=100)
    second_operand = fake.random_int(min=0, max=100)
    command = Add(first_operand, second_operand)
    assert command.execute() == first_operand + second_operand

def test_subtract_command():
    first_operand = fake.random_int(min=0, max=100)
    second_operand = fake.random_int(min=0, max=100)
    command = Subtract(first_operand, second_operand)
    assert command.execute() == first_operand - second_operand

def test_multiply_command():
    first_operand = fake.random_int(min=0, max=10)
    second_operand = fake.random_int(min=0, max=10)
    command = Multiply(first_operand, second_operand)
    assert command.execute() == first_operand * second_operand

#test division by non-zero numbers
def test_divide_command():
    first_operand = fake.random_int(min=1, max=100)
    second_operand = fake.random_int(min=1, max=10)
    command = Divide(first_operand, second_operand)
    assert command.execute() == first_operand / second_operand

#test division by zero
def test_divide_by_zero():
    operand1 = fake.random_int(min=1, max=100)
    command = Divide(operand1, 0)
    with pytest.raises(ValueError):
        command.execute()