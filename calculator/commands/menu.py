#  Bonus functionality :) 
# Displays a list of available commands. i.e - the commands defined in this folder

from .command import Command
def __init__(self, commands):
    self.commands = commands

def execute(self):
    print("\n Select a command:")
    for command in self.commands:
        print(f"- {command}")
    print("Type 'exit' to quit")