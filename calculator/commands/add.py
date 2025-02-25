#Inheirits from the Command base class to implement the addition operation via the execute method
from .command import Command

class Add(Command):
    def __init__(self, first_operand, second_operand):
        self.first_operand = first_operand
        self.second_operand = second_operand
    
    def execute(self):
        return self.first_operand + self.second_operand