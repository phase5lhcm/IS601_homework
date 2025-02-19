"""Calculator class encapsulates the behavior of math operations within a single class"""

from decimal import Decimal
from typing import Callable


class Calculation:
    def __init__(
        self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]
    ):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> Decimal:
        """Use to perform the math operation and returns the result"""
        return self.operation(self.a, self.b)

    @staticmethod
    def create(
        a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]
    ) -> "Calculation":
        return Calculation(a, b, operation)
