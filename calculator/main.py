from commands.add import Add
from commands.subtract import Subtract
from commands.multiply import Multiply
from commands.divide import Divide
from commands.menu import Menu
import importlib
import os

class Calculator:
    def __init__(self):
        self.commands = {
            'add': Add,
            'subtract': Subtract,
            'multiply': Multiply,
            'divide': Divide
        }
        self.load_plugins()
        self.commands['menu'] = Menu(self.commands)
    
    def load_plugins(self):
        plugins_directory = 'plugins'
        for file in os.listdir(plugins_directory):
            if file.endswith('.py') and file != '__init__.py':
                module_name = f"{plugins_directory}.{file[:-3]}"
                module = importlib.import_module(module_name)
                plugin = module.get_plugin()
                self.commands[plugin['name']] = plugin['class']
    def execute(self, command_name, operand1, operand2):
        command_class = self.commands.get(command_name)
        if command_class:
            command = command_class(operand1, operand2)
            return command.execute()
        else:
            print(f"Unknown command: {command_name}")

    
    def repl(self):
        print("Welcome to Command Pattern Calculator! Type 'menu' to see available commands.")
        while True:
            user_input = input("\nEnter command (e.g., add 2 3): ")
            if user_input.lower() == 'exit':
                print("Exiting...")
                break
            
            parts = user_input.split()
            if parts[0] == 'menu':
                self.commands['menu'].execute()
                continue

            if len(parts) == 3:
                command_name = parts[0]
                try:
                    operand1 = float(parts[1])
                    operand2 = float(parts[2])
                    result = self.execute(command_name, operand1, operand2)
                    print("Result:", result)
                except ValueError as e:
                    print("Error:", e)
            else:
                print("Invalid input format.")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.repl()