# Avneet_Kaur_IS601_MidtermCalculator

# Link to Video demo 
https://drive.google.com/file/d/1fUfTqW0qwdjN05fKcShcz3FkVPoJwtpA/view?usp=sharing

Overview

This is an advanced, Python-based command-line calculator designed for my project in IS601. It supports standard arithmetic operations, dynamic plugin integration, REPL interface, and robust calculation history management using Pandas. 

# Prerequisites

Ensure you have the following installed:

Python 3.10+
pip 
Git


# Installation

1. Clone the Repository

    
    git clone https://github.com/ak256-ak/Avneet_Kaur_IS601_Midterm_Calculator.git

    cd 

    Avneet_Kaur_IS601_Midterm_Calculator
    

2. Create a Virtual Environment**

    python3 -m venv venv
   

3. Install Dependencies

    
    pip install -r requirements.txt


# Setup

1. Environment Variables: 
   
   export LOG_LEVEL=DEBUG
   export LOG_FILE=calculator.log

# Starting the REPL

python3 repl.py

# History Management

Calculation history is stored in history.csv in the project directory.

 Use the history command in the REPL to view the saved calculations.

Use the clear_history command in the REPL to delete all history records.

# Running Tests

pip install pytest coverage

# Run Tests and Check Coverage

coverage run -m pytest
coverage report -m



# Running the Calculator

cd calculator

python3 calculator.py
