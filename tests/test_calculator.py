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
