from commands.add import Add
from commands.subtract import Subtract
from commands.multiply import Multiply
from commands.divide import Divide
from commands.menu import Menu
import importlib
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    filename="app.log",  # Saves logs to this file
    filemode="a" #Append mode
)

logger = logging.getLogger(__name__)
logger.info("Calculator App for IS601! Type 'menu' to see available commands or 'exit' to quit.")


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
    def execute(self, command_name, first_operand, second_operand):
        command_class = self.commands.get(command_name)
        if command_class:
            command = command_class(first_operand, second_operand)
            return command.execute()
        else:
            logger.warning(f"Unknown command: {command_name}")
            return "Unknown command. Use the menu for assistance"

    
    def repl(self):
        logger.info("Type 'menu' to see available commands.")
        while True:
            user_input = input("\nEnter command (e.g., add 2 3): ")
            if user_input.lower() == 'exit':
                logger.info("Exiting...")
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
                    logger.info(f"Result: {result}")
                except ValueError as e:
                    logger.error(f"Error loading plugin {module_name}: {e}")
            else:
                logger.warning("Invalid input format.")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.repl()