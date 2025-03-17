#Inheirits from the Command base class to implement the division operation via the execute method
from .command import Command
from ..utils.validator import Validator


class Divide(Command):
    def __init__(self, a,b):
        self.a = a
        self.b = b
    
    def execute(self):
        Validator.validate(self.b,"Cannot divide by zero" )
        return self.a / self.b