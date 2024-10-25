import importlib
import logging
import os
import sys
from history_manager import HistoryManagerFacade

# Set up logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(filename='calculator.log', level=LOG_LEVEL, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class OperationStrategy:
    """Strategy Pattern: Defines the operation interface"""
    def execute(self, a, b):
        raise NotImplementedError("This method should be overridden.")

class Calculator:
    """Main Calculator class with REPL and plugin integration"""

    def __init__(self):
        self.history_manager = HistoryManagerFacade("calculator_history.csv")
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        """Factory Pattern: Dynamically load plugins from 'plugins' folder"""
        plugins_folder = 'plugins'
        sys.path.insert(0, plugins_folder)
        
        for plugin in os.listdir(plugins_folder):
            if plugin.endswith('.py') and plugin != '__init__.py':
                module_name = plugin[:-3]
                try:
                    module = importlib.import_module(module_name)
                    operation = getattr(module, 'Operation')()
                    self.plugins[module_name] = operation
                    logging.info(f"Loaded plugin: {module_name}")
                except Exception as e:
                    logging.error(f"Error loading plugin {module_name}: {e}")

    def repl(self):
        """Read-Eval-Print Loop for calculator interaction"""
        print("Welcome to the Advanced Python Calculator!")
        print("Type 'exit' to quit, 'history' to view calculation history.")
        print("Available operations:", ", ".join(self.plugins.keys()))

        while True:
            command = input("\nEnter operation: ").strip().lower()
            if command == 'exit':
                print("Exiting the calculator. Goodbye!")
                break
            elif command == 'history':
                self.show_history()
                continue

            if command not in self.plugins:
                print("Invalid operation. Please try again.")
                continue

            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                result = self.plugins[command].execute(a, b)
                print(f"Result: {result}")
                self.history_manager.add_entry(command, a, b, result)
                logging.info(f"Operation: {command}, Operands: {a}, {b}, Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                logging.error("Invalid numeric input.")
            except Exception as e:
                print(f"Error: {e}")
                logging.error(f"Exception occurred: {e}")

    def show_history(self):
        """Displays the history of calculations"""
        try:
            history = self.history_manager.load_history()
            if history.empty:
                print("No history found.")
            else:
                print(history)
        except Exception as e:
            print(f"Error loading history: {e}")
            logging.error(f"Error loading history: {e}")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.repl()
'''
This is a test for the new branch 


'''