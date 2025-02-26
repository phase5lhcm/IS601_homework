# import pytest
# from calculator.calculator import Calculator

# @pytest.mark.parametrize("a, b, operation, expected", [
#     pytest.param(a, b, operation, expected) for a, b, operation, expected in []
# ])  # Empty list; pytest will use the fixture to populate it dynamically
# def test_operations(a, b, operation, expected, generate_test_data):
#     if operation == "add":
#         assert Calculator.add(a, b) == expected
#     elif operation == "subtract":
#         assert Calculator.subtract(a, b) == expected
#     elif operation == "multiply":
#         assert Calculator.multiply(a, b) == expected
#     elif operation == "divide":
#         assert Calculator.divide(a, b) == expected
