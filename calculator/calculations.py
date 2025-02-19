"""This module contains the calculator logic for performing arithmetic operations."""

from typing import List, Optional
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation:Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_latest(cls) -> Optional[Calculation]:
        """ Use to return the most recent calculation"""
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Use to to return a list of all calculations"""
        return cls.history
    
    @classmethod
    def clear_history(cls):
        """ Use to clear history list"""
        cls.history.clear()