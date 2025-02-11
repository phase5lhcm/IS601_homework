"""Calculator calss encapsulates the behavior of math operations within a single class"""

from decimal import Decimal
from typing impor Callable

class Calculation:
    def __init__(self, a:Decimal, d: Decimal, operation:Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
    
    """Use to perform the math operation and returns the result"""
    def perform(self) -> Decimal:
        return self.operation(self.a, self.b)

    @staticmethod
    def create(a:Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> "Calculation":
        return Calculation(a,b,operation)
