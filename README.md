
**# Avneet_Kaur_IS601_MidtermCalculator**

 # Link to Video Demo
 
https://drive.google.com/file/d/1fUfTqW0qwdjN05fKcShcz3FkVPoJwtpA/view?usp=sharing

 # Overview
This is an advanced, Pythonbased commandline calculator designed as a midterm project for IS601. It supports standard arithmetic operations, dynamic plugin integration, a REPL (ReadEvalPrint Loop) interface, and robust calculation history management using Pandas.

# Features
 Basic Operations: Add, Subtract, Multiply, Divide, Square, Cube, Exponent, Square Root.
 
 REPL Interface: Interactive commandline interface to execute operations in realtime.
 
 Dynamic Plugin System: Easily add new operations as plugins.
 
 History Management: Save, load, clear, and delete calculation history using CSV files.
 
 Logging: Comprehensive logging with dynamic configuration through environment variables.
 
 Design Patterns: Utilizes Factory, Facade, and Command patterns for modular and scalable code.

# Prerequisites

Ensure you have the following installed:

 Python 3.10+
 
 pip
 
 Git

# Installation

1. Clone the Repository
   
   git clone https://github.com/ak256ak/Avneet_Kaur_IS601_MidtermCalculator.git
   
2. cd Avneet_Kaur_IS601_MidtermCalculator
   

3. Create a Virtual Environment
   
   python3 m venv venv
   

4. Activate the Virtual Environment
    On macOS/Linux:
    
     source venv/bin/activate
     
    On Windows:
    
     .\venv\Scripts\activate
     

5. Install Dependencies
  
   pip install r requirements.txt
   

# Setup

1. Set Environment Variables
   
    Set up logging configuration:
   
     export LOG_LEVEL=DEBUG
   
     export LOG_FILE=calculator.log
     

# Starting the REPL Interface

 To start the calculator REPL interface:

  python3 calculator/calculator.py
  

 # The REPL interface supports the following 
   Basic Operations: add, subtract, multiply, divide, square, cube, exponent, squareroot
   
   History Management: history, save_history, load_history, clear_history, delete_history
   
   Other Commands: menu (shows available options), exit 


# History Management

 Calculation history is stored in calculator_history.csv in the project directory.
 
   Use the history command in the REPL to view saved calculations.
   
   Use the clear_history command in the REPL to delete all history records.

# Running Tests

1. Install testing tools:
   
   pip install pytest coverage
   

2. Run Tests and Check Coverage
   
    Run all tests:

     coverage run m pytest
     
  #  Generate coverage report:
     
     coverage report m
     
    Ensure total coverage is 90% or above(per instructions) 

# GitHub Actions Setup


1. Workflow File Location:
   
   The GitHub Actions workflow file is located in .github/workflows/pythonci.yml.
   
2.  CI Configuration:
    The CI pipeline installs dependencies, runs tests, and generates coverage reports.
   
3. How to Trigger CI:
    Push to the main  branch, or create a pull request to trigger the CI pipeline.

# Running the Calculator

1. Navigate to the calculator directory:
   
   Make sure you are in the correct folder
   
   cd calculator
   

2. Start the calculator:
   
   python3 calculator.py
   

# Design Patterns

 Factory Pattern: Used for dynamic plugin loading.
 
 Facade Pattern: Simplifies history management with Pandas.
 
 Command Pattern: Organizes REPL commands for clear command management.
 
 Links to code can be added for each pattern in the documentation.

# Error Handling
 The code uses both LBYL (Look Before You Leap) and EAFP (Easier to Ask for Forgiveness than Permission) strategies to handle potential errors effectively.
 
   Examples:
     LBYL: Checking if a file exists before reading it.
     
     EAFP: Using try/except blocks to catch exceptions when reading from a file.

 # Notes
 Make sure to **activate the virtual environment** before running the calculator or tests.
 
 The calculator log file will be created as calculator.log in the project directory.
 
________________________________________________________________________________________________________________________________________________________

# Project Design Overview

# Design Patterns

# Factory Pattern:

The factory pattern is used for dynamically loading plugins in the `Calculator` class, allowing the calculator to load operations without modifying the core code.

https://github.com/ak256-ak/Avneet_Kaur_IS601_MidtermCalculator/blob/main/calculator/calculator.py#L33

# Command Pattern:

The command pattern structures REPL commands, enabling consistent handling of operations like add, subtract, and history management. 

https://github.com/ak256-ak/Avneet_Kaur_IS601_MidtermCalculator/blob/main/calculator/calculator.py#L55

# Facade Pattern:

The facade pattern in `history_manager.py` provides a simplified interface for managing history operations

https://github.com/ak256-ak/Avneet_Kaur_IS601_MidtermCalculator/blob/main/calculator/history_manager.py#L15

# Environment Variables:

Environment variables like `LOG_LEVEL` and `LOG_FILE` are used for dynamically configuring logging behavior, setting the logging level and specifying the log file.

https://github.com/ak256-ak/Avneet_Kaur_IS601_MidtermCalculator/blob/main/calculator/calculator.py#L10

# Logging Implementation:

Python's logging module is used to record events, errors, and information, dynamically configured via environment variables. Logs are recorded in calculator.log. 

https://github.com/ak256-ak/Avneet_Kaur_IS601_MidtermCalculator/blob/main/calculator/calculator.py#L12

https://github.com/ak256-ak/Avneet_Kaur_IS601_MidtermCalculator/blob/main/calculator/history_manager.py#L18

# Try Implementation for LBYL and EAFP: 

LBYL (Look Before You Leap): Conditions are checked before performing an action, like verifying file existence before reading. 

https://github.com/ak256-ak/Avneet_Kaur_IS601_MidtermCalculator/blob/main/calculator/history_manager.py#L50

EAFP  EAFP is used to handle unexpected errors by trying an operation and catching exceptions. 

https://github.com/ak256-ak/Avneet_Kaur_IS601_MidtermCalculator/blob/main/calculator/calculator.py#L180





