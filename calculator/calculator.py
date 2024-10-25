

'''
The below code is good 

'''
'''
import importlib
import logging
import os
import sys
from history_manager import HistoryManagerFacade

# Set up logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
LOG_FILE = os.getenv("LOG_FILE", "calculator.log")
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    """Main Calculator class with REPL and plugin integration"""

    def __init__(self):
        self.history_manager = HistoryManagerFacade("calculator_history.csv")
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        """Factory Pattern: Dynamically load plugins from 'plugins' folder"""
        plugins_folder = 'calculator/plugins'
        sys.path.insert(0, plugins_folder)
        
        if not os.path.exists(plugins_folder):
            os.makedirs(plugins_folder)
        
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
            elif command == 'save_history':
                self.history_manager.save_history()
                print("History saved.")
                continue
            elif command == 'clear_history':
                self.history_manager.clear_history()
                print("History cleared.")
                continue
            elif command == 'delete_history':
                self.history_manager.delete_history()
                print("History deleted.")
                continue

            if command not in self.plugins:
                print("Invalid operation. Please try again.")
                continue

            try:
                a = float(input("Enter the first number: "))
                b = None
                if command not in ['square', 'squareroot', 'cube']:
                    b = float(input("Enter the second number: "))

                result = self.plugins[command].execute(a, b)
                print(f"Result: {result}")
                self.history_manager.add_entry(command, a, b, result)
                logging.info(f"Operation: {command}, Operands: {a}, {b}, Result: {result}")
            except ValueError as ve:
                print(f"Error: {ve}")
                logging.error(f"Value error: {ve}")
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
'''
This is a test for the new repo 


'''


'''

The below code is good and pushed 
'''
'''

import importlib
import logging
import os
import sys
from history_manager import HistoryManagerFacade

# Set up logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
LOG_FILE = os.getenv("LOG_FILE", "calculator.log")
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    """Main Calculator class with REPL and plugin integration"""

    def __init__(self):
        self.history_manager = HistoryManagerFacade("calculator_history.csv")
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        """Factory Pattern: Dynamically load plugins from 'plugins' folder"""
        plugins_folder = 'calculator/plugins'
        sys.path.insert(0, plugins_folder)
        
        if not os.path.exists(plugins_folder):
            os.makedirs(plugins_folder)
        
        for plugin in os.listdir(plugins_folder):
            if plugin.endswith('.py') and plugin != '__init__.py':
                module_name = plugin[:-3]
                try:
                    module = importlib.import_module(module_name)
                    operation = getattr(module, 'Operation')()
                    self.plugins[module_name] = operation
                    logging.info(f"Loaded plugin: {module_name}")
                except ImportError as e:
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
            elif command == 'save_history':
                self.history_manager.save_history()
                print("History saved.")
                continue
            elif command == 'clear_history':
                self.history_manager.clear_history()
                print("History cleared.")
                continue
            elif command == 'delete_history':
                self.history_manager.delete_history()
                print("History deleted.")
                continue

            if command not in self.plugins:
                print("Invalid operation. Please try again.")
                continue

            try:
                a = float(input("Enter the first number: "))
                b = None
                if command not in ['square', 'squareroot', 'cube']:
                    b = float(input("Enter the second number: "))

                result = self.plugins[command].execute(a, b)
                print(f"Result: {result}")
                self.history_manager.add_entry(command, a, b, result)
                logging.info(f"Operation: {command}, Operands: {a}, {b}, Result: {result}")
            except ValueError as ve:
                print("Invalid input. Please enter numeric values.")
                logging.error(f"Value error: {ve}")
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

'''
The below code is a test to see if i can perform calculations
'''

'''
This code is working and good for eveyething but load_history but this code has been puished to git 
'''


'''

import importlib
import logging
import os
import sys
from history_manager import HistoryManagerFacade

# Set up logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
LOG_FILE = os.getenv("LOG_FILE", "calculator.log")
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    """Main Calculator class with REPL and plugin integration"""

    def __init__(self):
        self.history_manager = HistoryManagerFacade("calculator_history.csv")
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        """Factory Pattern: Dynamically load plugins from 'plugins' folder"""
        plugins_folder = 'calculator/plugins'
        sys.path.insert(0, plugins_folder)
        
        if not os.path.exists(plugins_folder):
            os.makedirs(plugins_folder)
        
        for plugin in os.listdir(plugins_folder):
            if plugin.endswith('.py') and plugin != '__init__.py':
                module_name = plugin[:-3]
                try:
                    module = importlib.import_module(module_name)
                    operation = getattr(module, 'Operation')()
                    self.plugins[module_name] = operation
                    logging.info(f"Loaded plugin: {module_name}")
                except ImportError as e:
                    logging.error(f"Error loading plugin {module_name}: {e}")

    def repl(self):
        """Read-Eval-Print Loop for calculator interaction"""
        print("\n" + "="*40)
        print(" Welcome to the Advanced Python Calculator ")
        print("="*40)
        print("\nPlease choose one of the following options:")
        self.show_menu()

        while True:
            command = input("\nEnter command: ").strip().lower()

            if command == 'exit':
                print("\nThank you for using the calculator!")
                break
            elif command == 'menu':
                self.show_menu()
                continue
            elif command == 'history':
                self.show_history()
                continue
            elif command == 'save_history':
                self.history_manager.save_history()
                print("\nHistory saved.")
                continue
            elif command == 'clear_history':
                self.history_manager.clear_history()
                print("\nHistory cleared.")
                continue
            elif command == 'delete_history':
                self.history_manager.delete_history()
                print("\nHistory deleted.")
                continue

            if command not in self.plugins:
                print("\nInvalid command. Type 'menu' to see available options or 'exit' to quit.")
                continue

            try:
                a = float(input("Enter the first number: "))
                b = None
                if command not in ['square', 'squareroot', 'cube']:
                    b = float(input("Enter the second number: "))

                result = self.plugins[command].execute(a, b)
                print(f"\nResult: {result}")
                self.history_manager.add_entry(command, a, b, result)
                logging.info(f"Operation: {command}, Operands: {a}, {b}, Result: {result}")
            except ValueError as ve:
                print("\nInvalid input. Please enter numeric values.")
                logging.error(f"Value error: {ve}")
            except Exception as e:
                print(f"\nError: {e}")
                logging.error(f"Exception occurred: {e}")

    def show_menu(self):
        """Display available commands to the user"""
        print("\n" + "-"*40)
        print("Basic Operations:")
        print(" add\n subtract\n multiply\n divide\n cube\n square\n exponent\n squareroot")
        print("\nHistory Management:")
        print(" history\n save_history\n load_history\n clear_history\n delete_history")
        print("\nOther Commands:")
        print(" menu - See available options")
        print(" exit - Quit the calculator")
        print("-"*40)

    def show_history(self):
        """Displays the history of calculations"""
        try:
            history = self.history_manager.load_history()
            if history.empty:
                print("\nNo history found.")
            else:
                print("\nCalculation History:")
                print(history)
        except Exception as e:
            print(f"\nError loading history: {e}")
            logging.error(f"Error loading history: {e}")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.repl()

'''



'''
The belwo code makes load_history work as well
'''
'''

import importlib
import logging
import os
import sys
from history_manager import HistoryManagerFacade

# Set up logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
LOG_FILE = os.getenv("LOG_FILE", "calculator.log")
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    """Main Calculator class with REPL and plugin integration"""

    def __init__(self):
        self.history_manager = HistoryManagerFacade("calculator_history.csv")
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        """Factory Pattern: Dynamically load plugins from 'plugins' folder"""
        plugins_folder = 'calculator/plugins'
        sys.path.insert(0, plugins_folder)
        
        if not os.path.exists(plugins_folder):
            os.makedirs(plugins_folder)
        
        for plugin in os.listdir(plugins_folder):
            if plugin.endswith('.py') and plugin != '__init__.py':
                module_name = plugin[:-3]
                try:
                    module = importlib.import_module(module_name)
                    operation = getattr(module, 'Operation')()
                    self.plugins[module_name] = operation
                    logging.info(f"Loaded plugin: {module_name}")
                except ImportError as e:
                    logging.error(f"Error loading plugin {module_name}: {e}")

    def repl(self):
        """Read-Eval-Print Loop for calculator interaction"""
        print("\n" + "="*40)
        print(" Welcome to the Advanced Python Calculator ")
        print("="*40)
        print("\nPlease choose one of the following options:")
        self.show_menu()

        while True:
            command = input("\nEnter command: ").strip().lower()

            if command == 'exit':
                print("\nThank you for using the calculator!")
                break
            elif command == 'menu':
                self.show_menu()
                continue
            elif command == 'history':
                self.show_history()
                continue
            elif command == 'save_history':
                self.history_manager.save_history()
                print("\nHistory saved.")
                continue
            elif command == 'load_history':
                self.load_history()
                continue
            elif command == 'clear_history':
                self.history_manager.clear_history()
                print("\nHistory cleared.")
                continue
            elif command == 'delete_history':
                self.history_manager.delete_history()
                print("\nHistory deleted.")
                continue

            if command not in self.plugins:
                print("\nInvalid command. Type 'menu' to see available options or 'exit' to quit.")
                continue

            try:
                a = float(input("Enter the first number: "))
                b = None
                if command not in ['square', 'squareroot', 'cube']:
                    b = float(input("Enter the second number: "))

                result = self.plugins[command].execute(a, b)
                print(f"\nResult: {result}")
                self.history_manager.add_entry(command, a, b, result)
                logging.info(f"Operation: {command}, Operands: {a}, {b}, Result: {result}")
            except ValueError as ve:
                print("\nInvalid input. Please enter numeric values.")
                logging.error(f"Value error: {ve}")
            except Exception as e:
                print(f"\nError: {e}")
                logging.error(f"Exception occurred: {e}")

    def show_menu(self):
        """Display available commands to the user"""
        print("\n" + "-"*40)
        print("Basic Operations:")
        print(" add\n subtract\n multiply\n divide\n cube\n square\n exponent\n squareroot")
        print("\nHistory Management:")
        print(" history\n save_history\n load_history\n clear_history\n delete_history")
        print("\nOther Commands:")
        print(" menu - See available options")
        print(" exit - Quit the calculator")
        print("-"*40)

    def show_history(self):
        """Displays the history of calculations"""
        try:
            history = self.history_manager.load_history()
            if history.empty:
                print("\nNo history found.")
            else:
                print("\nCalculation History:")
                print(history)
        except Exception as e:
            print(f"\nError loading history: {e}")
            logging.error(f"Error loading history: {e}")

    def load_history(self):
        """Load and display history from the CSV file"""
        try:
            history = self.history_manager.load_history()
            if history.empty:
                print("\nNo history found to load.")
            else:
                print("\nLoaded History:")
                print(history)
        except Exception as e:
            print(f"\nError loading history: {e}")
            logging.error(f"Error loading history: {e}")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.repl()
'''

'''
testing this below code to see if it works 
'''

import importlib
import logging
import os
import sys
from history_manager import HistoryManagerFacade

# Set up logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
LOG_FILE = os.getenv("LOG_FILE", "calculator.log")
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    """Main Calculator class with REPL and plugin integration"""

    def __init__(self):
        self.history_manager = HistoryManagerFacade("calculator_history.csv")
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        """Factory Pattern: Dynamically load plugins from 'plugins' folder"""
        plugins_folder = os.path.join(os.path.dirname(__file__), 'plugins')
        sys.path.insert(0, plugins_folder)

        if not os.path.exists(plugins_folder):
            os.makedirs(plugins_folder)

        for plugin in os.listdir(plugins_folder):
            if plugin.endswith('.py') and plugin != '__init__.py':
                module_name = plugin[:-3]
                try:
                    module = importlib.import_module(module_name)
                    operation = getattr(module, 'Operation')()
                    self.plugins[module_name] = operation
                    logging.info(f"Loaded plugin: {module_name}")
                    print(f"Loaded plugin: {module_name}")  # Debugging output
                except ImportError as e:
                    logging.error(f"Error loading plugin {module_name}: {e}")
                    print(f"Error loading plugin {module_name}: {e}")  # Debugging output

        # Print all loaded plugins for verification
        print(f"Loaded Plugins: {list(self.plugins.keys())}")

    def repl(self):
        """Read-Eval-Print Loop for calculator interaction"""
        print("\n" + "="*40)
        print(" Welcome to the Advanced Python Calculator ")
        print("="*40)
        print("\nPlease choose one of the following options:")
        self.show_menu()

        while True:
            command = input("\nEnter command: ").strip().lower()
            print(f"Received command: '{command}'")  # Debugging output

            if command == 'exit':
                print("\nThank you for using the calculator!")
                break
            elif command == 'menu':
                self.show_menu()
                continue
            elif command == 'history':
                self.show_history()
                continue
            elif command == 'save_history':
                self.history_manager.save_history()
                print("\nHistory saved.")
                continue
            elif command == 'load_history':
                self.load_history()
                continue
            elif command == 'clear_history':
                self.history_manager.clear_history()
                print("\nHistory cleared.")
                continue
            elif command == 'delete_history':
                self.history_manager.delete_history()
                print("\nHistory deleted.")
                continue

            if command not in self.plugins:
                print("\nInvalid command. Type 'menu' to see available options or 'exit' to quit.")
                continue

            try:
                a = float(input("Enter the first number: "))
                b = None
                if command not in ['square', 'squareroot', 'cube']:
                    b = float(input("Enter the second number: "))

                result = self.plugins[command].execute(a, b)
                print(f"\nResult: {result}")
                self.history_manager.add_entry(command, a, b, result)
                logging.info(f"Operation: {command}, Operands: {a}, {b}, Result: {result}")
            except ValueError as ve:
                print("\nInvalid input. Please enter numeric values.")
                logging.error(f"Value error: {ve}")
            except Exception as e:
                print(f"\nError: {e}")
                logging.error(f"Exception occurred: {e}")

    def show_menu(self):
        """Display available commands to the user"""
        print("\n" + "-"*40)
        print("Basic Operations:")
        print(" add\n subtract\n multiply\n divide\n cube\n square\n exponent\n squareroot")
        print("\nHistory Management:")
        print(" history\n save_history\n load_history\n clear_history\n delete_history")
        print("\nOther Commands:")
        print(" menu - See available options")
        print(" exit - Quit the calculator")
        print("-"*40)

    def show_history(self):
        """Displays the history of calculations"""
        try:
            history = self.history_manager.load_history()
            if history.empty:
                print("\nNo history found.")
            else:
                print("\nCalculation History:")
                print(history)
        except Exception as e:
            print(f"\nError loading history: {e}")
            logging.error(f"Error loading history: {e}")

    def load_history(self):
        """Load and display history from the CSV file"""
        try:
            history = self.history_manager.load_history()
            if history.empty:
                print("\nNo history found to load.")
            else:
                print("\nLoaded History:")
                print(history)
        except Exception as e:
            print(f"\nError loading history: {e}")
            logging.error(f"Error loading history: {e}")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.repl()
