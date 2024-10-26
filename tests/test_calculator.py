'''
The below codes provides 68% covergae but it passes all the test,mind you it only has two files test_cacl and test_history_manager
'''

'''
import pytest
import sys
import os

# Add the calculator directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator')))

from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    result = calculator.plugins['add'].execute(3, 2)
    assert result == 5

def test_subtract(calculator):
    result = calculator.plugins['subtract'].execute(5, 3)
    assert result == 2

def test_multiply(calculator):
    result = calculator.plugins['multiply'].execute(4, 3)
    assert result == 12

def test_divide(calculator):
    result = calculator.plugins['divide'].execute(10, 2)
    assert result == 5

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.plugins['divide'].execute(10, 0)

def test_square(calculator):
    result = calculator.plugins['square'].execute(4)
    assert result == 16

def test_exponent(calculator):
    result = calculator.plugins['exponent'].execute(2, 3)
    assert result == 8

def test_squareroot(calculator):
    result = calculator.plugins['squareroot'].execute(9)
    assert result == 3

def test_squareroot_negative(calculator):
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number."):
        calculator.plugins['squareroot'].execute(-9)

def test_cube(calculator):
    result = calculator.plugins['cube'].execute(3)
    assert result == 27


'''


''' The below code is better since it took covergae from 68 to 83'''

'''
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator')))
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_repl_exit(calculator, monkeypatch):
    """Test REPL exit command"""
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()

def test_invalid_operation(calculator, monkeypatch, capsys):
    """Test invalid operation in REPL"""
    inputs = iter(['invalid_op', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "Invalid operation. Please try again." in captured.out

def test_show_history(calculator, capsys):
    """Test showing history"""
    calculator.history_manager.add_entry('add', 2, 3, 5)
    calculator.show_history()
    captured = capsys.readouterr()
    assert "add" in captured.out
    assert "2" in captured.out
    assert "5" in captured.out

def test_plugin_loading_error(monkeypatch):
    """Simulate a plugin loading error"""
    def mock_import_module(name):
        raise ImportError("Simulated ImportError")

    monkeypatch.setattr('importlib.import_module', mock_import_module)
    calc = Calculator()
    calc.load_plugins()  # Attempt to load plugins with the simulated error
    assert len(calc.plugins) == 0  # No plugins should be loaded

def test_successful_plugin_load(calculator):
    """Test successful plugin loading"""
    assert 'add' in calculator.plugins
    assert 'subtract' in calculator.plugins
    assert 'multiply' in calculator.plugins
    assert 'divide' in calculator.plugins

def test_add_operation(calculator):
    """Test add operation plugin"""
    result = calculator.plugins['add'].execute(3, 2)
    assert result == 5

def test_subtract_operation(calculator):
    """Test subtract operation plugin"""
    result = calculator.plugins['subtract'].execute(5, 2)
    assert result == 3

def test_multiply_operation(calculator):
    """Test multiply operation plugin"""
    result = calculator.plugins['multiply'].execute(5, 2)
    assert result == 10

def test_divide_operation(calculator):
    """Test divide operation plugin"""
    result = calculator.plugins['divide'].execute(10, 2)
    assert result == 5

def test_divide_by_zero(calculator):
    """Test divide by zero handling"""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.plugins['divide'].execute(10, 0)

def test_square_operation(calculator):
    """Test square operation plugin"""
    result = calculator.plugins['square'].execute(4)
    assert result == 16

def test_exponent_operation(calculator):
    """Test exponent operation plugin"""
    result = calculator.plugins['exponent'].execute(2, 3)
    assert result == 8

def test_squareroot_operation(calculator):
    """Test square root operation plugin"""
    result = calculator.plugins['squareroot'].execute(9)
    assert result == 3

def test_squareroot_negative(calculator):
    """Test square root of a negative number"""
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number."):
        calculator.plugins['squareroot'].execute(-9)

def test_cube_operation(calculator):
    """Test cube operation plugin"""
    result = calculator.plugins['cube'].execute(3)
    assert result == 27
'''


'''
Testing the below code to see if it take covergae up 
well this took the coverage to 85% 
'''


'''

import pytest
import sys
import os

# Set up path to access the calculator module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator')))
from calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture for initializing the calculator instance"""
    return Calculator()

def test_add_operation(calculator):
    """Test add operation plugin"""
    result = calculator.plugins['add'].execute(3, 2)
    assert result == 5

def test_subtract_operation(calculator):
    """Test subtract operation plugin"""
    result = calculator.plugins['subtract'].execute(5, 2)
    assert result == 3

def test_multiply_operation(calculator):
    """Test multiply operation plugin"""
    result = calculator.plugins['multiply'].execute(4, 2)
    assert result == 8

def test_divide_operation(calculator):
    """Test divide operation plugin"""
    result = calculator.plugins['divide'].execute(10, 2)
    assert result == 5

def test_divide_by_zero(calculator):
    """Test divide by zero handling"""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.plugins['divide'].execute(10, 0)

def test_square_operation(calculator):
    """Test square operation plugin"""
    result = calculator.plugins['square'].execute(4)
    assert result == 16

def test_exponent_operation(calculator):
    """Test exponent operation plugin"""
    result = calculator.plugins['exponent'].execute(2, 3)
    assert result == 8

def test_squareroot_operation(calculator):
    """Test square root operation plugin"""
    result = calculator.plugins['squareroot'].execute(9)
    assert result == 3

def test_squareroot_negative(calculator):
    """Test square root of a negative number"""
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number."):
        calculator.plugins['squareroot'].execute(-9)

def test_cube_operation(calculator):
    """Test cube operation plugin"""
    result = calculator.plugins['cube'].execute(3)
    assert result == 27

# New tests for REPL commands

def test_repl_show_history(calculator, monkeypatch, capsys):
    """Test REPL command for showing history"""
    calculator.history_manager.add_entry('multiply', 4, 2, 8)
    inputs = iter(['history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "multiply" in captured.out

def test_repl_clear_history(calculator, monkeypatch, capsys):
    """Test REPL command for clearing history"""
    calculator.history_manager.add_entry('add', 1, 2, 3)
    inputs = iter(['clear_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "History cleared." in captured.out

def test_repl_save_history(calculator, monkeypatch, capsys):
    """Test REPL command for saving history"""
    inputs = iter(['save_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "History saved." in captured.out

def test_repl_delete_history(calculator, monkeypatch, capsys):
    """Test REPL command for deleting history"""
    inputs = iter(['delete_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "History deleted." in captured.out

'''


'''
The below code is there for test purpose to see if ocvergae goes up 
'''

'''
The coverge did go up 
'''

'''


import pytest
import sys
import os

# Set up path to access the calculator module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator')))
from calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture for initializing the calculator instance"""
    return Calculator()

def test_add_operation(calculator):
    """Test add operation plugin"""
    result = calculator.plugins['add'].execute(3, 2)
    assert result == 5

def test_subtract_operation(calculator):
    """Test subtract operation plugin"""
    result = calculator.plugins['subtract'].execute(5, 2)
    assert result == 3

def test_multiply_operation(calculator):
    """Test multiply operation plugin"""
    result = calculator.plugins['multiply'].execute(4, 2)
    assert result == 8

def test_divide_operation(calculator):
    """Test divide operation plugin"""
    result = calculator.plugins['divide'].execute(10, 2)
    assert result == 5

def test_divide_by_zero(calculator):
    """Test divide by zero handling"""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.plugins['divide'].execute(10, 0)

def test_square_operation(calculator):
    """Test square operation plugin"""
    result = calculator.plugins['square'].execute(4)
    assert result == 16

def test_exponent_operation(calculator):
    """Test exponent operation plugin"""
    result = calculator.plugins['exponent'].execute(2, 3)
    assert result == 8

def test_squareroot_operation(calculator):
    """Test square root operation plugin"""
    result = calculator.plugins['squareroot'].execute(9)
    assert result == 3

def test_squareroot_negative(calculator):
    """Test square root of a negative number"""
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number."):
        calculator.plugins['squareroot'].execute(-9)

def test_cube_operation(calculator):
    """Test cube operation plugin"""
    result = calculator.plugins['cube'].execute(3)
    assert result == 27

# New tests for REPL commands and error handling

def test_repl_show_history(calculator, monkeypatch, capsys):
    """Test REPL command for showing history"""
    calculator.history_manager.add_entry('multiply', 4, 2, 8)
    inputs = iter(['history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "multiply" in captured.out

def test_repl_clear_history(calculator, monkeypatch, capsys):
    """Test REPL command for clearing history"""
    calculator.history_manager.add_entry('add', 1, 2, 3)
    inputs = iter(['clear_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "History cleared." in captured.out

def test_repl_save_history(calculator, monkeypatch, capsys):
    """Test REPL command for saving history"""
    inputs = iter(['save_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "History saved." in captured.out

def test_repl_delete_history(calculator, monkeypatch, capsys):
    """Test REPL command for deleting history"""
    inputs = iter(['delete_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "History deleted." in captured.out

def test_repl_invalid_input(calculator, monkeypatch, capsys):
    """Test REPL with invalid numeric input"""
    inputs = iter(['add', 'invalid', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numeric values." in captured.out

def test_repl_plugin_loading_error(monkeypatch):
    """Simulate an error during plugin loading"""
    def mock_import_module(name):
        raise ImportError("Simulated ImportError")
    
    monkeypatch.setattr('importlib.import_module', mock_import_module)
    calc = Calculator()
    calc.load_plugins()
    assert len(calc.plugins) == 0  # Plugins should not load
'''



'''

The below code adds load_history to check for covergae 

'''

import pytest
import sys
import os

# Set up path to access the calculator module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator')))
from calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture for initializing the calculator instance"""
    return Calculator()

# Basic operation tests
def test_add_operation(calculator):
    """Test add operation plugin"""
    result = calculator.plugins['add'].execute(3, 2)
    assert result == 5

def test_subtract_operation(calculator):
    """Test subtract operation plugin"""
    result = calculator.plugins['subtract'].execute(5, 2)
    assert result == 3

def test_multiply_operation(calculator):
    """Test multiply operation plugin"""
    result = calculator.plugins['multiply'].execute(4, 2)
    assert result == 8

def test_divide_operation(calculator):
    """Test divide operation plugin"""
    result = calculator.plugins['divide'].execute(10, 2)
    assert result == 5

def test_divide_by_zero(calculator):
    """Test divide by zero handling"""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.plugins['divide'].execute(10, 0)

def test_square_operation(calculator):
    """Test square operation plugin"""
    result = calculator.plugins['square'].execute(4)
    assert result == 16

def test_exponent_operation(calculator):
    """Test exponent operation plugin"""
    result = calculator.plugins['exponent'].execute(2, 3)
    assert result == 8

def test_squareroot_operation(calculator):
    """Test square root operation plugin"""
    result = calculator.plugins['squareroot'].execute(9)
    assert result == 3

def test_squareroot_negative(calculator):
    """Test square root of a negative number"""
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number."):
        calculator.plugins['squareroot'].execute(-9)

def test_cube_operation(calculator):
    """Test cube operation plugin"""
    result = calculator.plugins['cube'].execute(3)
    assert result == 27

# REPL command tests

def test_repl_show_history(calculator, monkeypatch, capsys):
    """Test REPL command for showing history"""
    calculator.history_manager.add_entry('multiply', 4, 2, 8)
    inputs = iter(['history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "multiply" in captured.out

def test_repl_clear_history(calculator, monkeypatch, capsys):
    """Test REPL command for clearing history"""
    calculator.history_manager.add_entry('add', 1, 2, 3)
    inputs = iter(['clear_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "History cleared." in captured.out

def test_repl_save_history(calculator, monkeypatch, capsys):
    """Test REPL command for saving history"""
    inputs = iter(['save_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "History saved." in captured.out

def test_repl_load_history(calculator, monkeypatch, capsys):
    """Test REPL command for loading history"""
    calculator.history_manager.add_entry('add', 1, 2, 3)
    calculator.history_manager.save_history()
    inputs = iter(['load_history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "Loaded History:" in captured.out

def test_repl_invalid_numeric_input(calculator, monkeypatch, capsys):
    """Test REPL with invalid numeric input"""
    inputs = iter(['add', 'invalid', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numeric values." in captured.out

def test_repl_invalid_command(calculator, monkeypatch, capsys):
    """Test REPL with an invalid command"""
    inputs = iter(['invalid_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "Invalid command" in captured.out

def test_repl_general_exception(calculator, monkeypatch, capsys):
    """Test REPL handling of general exceptions"""
    def mock_execute(*args, **kwargs):
        raise Exception("Simulated exception")
    
    monkeypatch.setattr(calculator.plugins['add'], 'execute', mock_execute)
    inputs = iter(['add', '1', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calculator.repl()
    captured = capsys.readouterr()
    assert "Error: Simulated exception" in captured.out
