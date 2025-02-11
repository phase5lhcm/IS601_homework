from typing import List, Optional
from calculator.calculation import calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation:Calculation):
        cls.history.append(calculation)

   """ Use to return the most recen calculation"""
    @classmethod
    def get_latest(cls) -> Optional[Calculation]:
        return cls.history[-1] if cls.history else None

    """Use to to return a list of all calculations"""
    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    """ Use to clear history list"""
    @classmethod
    def clear_history(cls):
        cls.history.clear()