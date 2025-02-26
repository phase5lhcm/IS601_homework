#Using plugins helps us maintain the Open/Closed Principle byadding new commands dynamically without altering the core code of the calculator application
#This plugin calculates the percentage of one number relative to another

from commands.command import Command
from utils.validator import Validator

class PercentageCommand(Command):
    def __init__(self, first_operand, second_operand):
        self.first_operand = first_operand
        self.second_operand = second_operand

    def execute(self):
        Validator.validate(self.second_operand,"The second operand must be greater than zero" )
        return (self.first_operand / self.second_operand) * 100
    
    def get_plugin():
        return{
            'name': 'percentage',
            'class': PercentageCommand
        }