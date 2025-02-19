import pytest
from decimal import Decimal
from faker import Faker
import random

faker = Faker()

def pytest_addoption(parser):
    """Add a custom command-line option to specify the number of records."""
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records to generate")


@pytest.fixture(scope="session")
def num_records(request):
    """Fixture to retrieve the number of test records from the command line."""
    return request.config.getoption("--num_records")


@pytest.fixture(scope="session")
def generate_test_data(num_records):
    """Generate test data dynamically based on the number of records requested."""
    operations = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: a / b if b != 0 else None,  # Avoid division by zero
    }

    test_cases = []
    
    for _ in range(num_records):
        a = Decimal(faker.random_int(min=-100, max=100))
        b = Decimal(faker.random_int(min=-100, max=100))
        operation = random.choice(list(operations.keys()))
        
        if operation == "divide" and b == 0:  # Ensure no zero division
            b = Decimal(1)

        expected = operations[operation](a, b)
        test_cases.append((a, b, operation, expected))
    
    return test_cases
