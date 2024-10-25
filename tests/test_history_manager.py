'''
The below codes provides 68% covergae but it passes all the test,mind you it only has two files test_cacl and test_history_manager
'''

'''

import pytest
import os
import sys

# Add the calculator directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator')))

from history_manager import HistoryManagerFacade

@pytest.fixture
def history_manager():
    return HistoryManagerFacade('test_history.csv')

def test_add_entry(history_manager):
    history_manager.add_entry('add', 3, 2, 5)
    df = history_manager.load_history()
    assert not df.empty
    assert df.iloc[-1]['Operation'] == 'add'
    assert df.iloc[-1]['Operand1'] == 3
    assert df.iloc[-1]['Operand2'] == 2
    assert df.iloc[-1]['Result'] == 5

def test_load_history(history_manager):
    history_manager.add_entry('multiply', 4, 2, 8)
    df = history_manager.load_history()
    assert not df.empty

def test_clear_history(history_manager):
    history_manager.clear_history()
    df = history_manager.load_history()
    assert df.empty

def test_delete_history(history_manager):
    history_manager.delete_history()
    assert not os.path.exists('test_history.csv')
'''

''' The below code is better since it took covergae from 68 to 83'''
'''
import pytest
import os
import pandas as pd
from history_manager import HistoryManagerFacade

@pytest.fixture
def history_manager():
    # Use a temporary CSV file for testing
    return HistoryManagerFacade('test_history.csv')

def test_initialize_file(history_manager):
    """Test file initialization"""
    if os.path.exists('test_history.csv'):
        os.remove('test_history.csv')  # Remove if exists
    history_manager._initialize_file()
    assert os.path.exists('test_history.csv')

def test_add_entry(history_manager):
    """Test adding an entry to history"""
    history_manager.add_entry('add', 2, 3, 5)
    df = history_manager.load_history()
    assert not df.empty
    assert df.iloc[-1]['Operation'] == 'add'
    assert df.iloc[-1]['Operand1'] == 2
    assert df.iloc[-1]['Operand2'] == 3
    assert df.iloc[-1]['Result'] == 5

def test_add_entry_exception(monkeypatch, history_manager):
    """Simulate an error while adding an entry"""
    def mock_to_csv(*args, **kwargs):
        raise IOError("Simulated IOError")
    
    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)
    try:
        history_manager.add_entry('add', 2, 3, 5)
    except Exception as e:
        assert str(e) == "Simulated IOError"

def test_load_history(history_manager):
    """Test loading history"""
    history_manager.add_entry('multiply', 4, 2, 8)
    df = history_manager.load_history()
    assert not df.empty
    assert 'multiply' in df['Operation'].values

def test_clear_history(history_manager):
    """Test clearing history"""
    history_manager.clear_history()
    df = history_manager.load_history()
    assert df.empty

def test_save_history_exception(monkeypatch, history_manager):
    """Simulate an error while saving history"""
    def mock_to_csv(*args, **kwargs):
        raise IOError("Simulated IOError")

    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)
    try:
        history_manager.save_history()
    except Exception as e:
        assert str(e) == "Simulated IOError"

def test_delete_history(history_manager):
    """Test deleting history file"""
    history_manager.delete_history()
    assert not os.path.exists('test_history.csv')

def test_delete_history_exception(monkeypatch, history_manager):
    """Simulate an error while deleting history"""
    def mock_remove(*args, **kwargs):
        raise OSError("Simulated OSError")

    monkeypatch.setattr(os, 'remove', mock_remove)
    try:
        history_manager.delete_history()
    except Exception as e:
        assert str(e) == "Simulated OSError"
'''

'''
Testing the below code to see if it helps with coverage 
'''

import pytest
import os
import pandas as pd
from history_manager import HistoryManagerFacade

@pytest.fixture
def history_manager():
    """Fixture for initializing the history manager"""
    return HistoryManagerFacade('test_history.csv')

def test_add_entry(history_manager):
    """Test adding an entry to history"""
    history_manager.add_entry('add', 1, 2, 3)
    df = history_manager.load_history()
    assert not df.empty
    assert 'add' in df['Operation'].values

def test_clear_history(history_manager):
    """Test clearing history"""
    history_manager.add_entry('add', 1, 2, 3)
    history_manager.clear_history()
    df = history_manager.load_history()
    assert df.empty

def test_load_history_empty(history_manager):
    """Test loading history when file is empty"""
    history_manager.clear_history()
    df = history_manager.load_history()
    assert df.empty

def test_load_history_error(monkeypatch, history_manager):
    """Simulate error when loading history"""
    def mock_read_csv(*args, **kwargs):
        raise pd.errors.EmptyDataError("Simulated error")

    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)
    df = history_manager.load_history()
    assert df.empty

def test_save_history_error(monkeypatch, history_manager):
    """Simulate error when saving history"""
    def mock_to_csv(*args, **kwargs):
        raise IOError("Simulated IOError")

    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)
    with pytest.raises(IOError, match="Simulated IOError"):
        history_manager.save_history()

def test_clear_history_error(monkeypatch, history_manager):
    """Simulate error when clearing history"""
    def mock_to_csv(*args, **kwargs):
        raise IOError("Simulated IOError")

    monkeypatch.setattr(pd.DataFrame, 'to_csv', mock_to_csv)
    with pytest.raises(IOError, match="Simulated IOError"):
        history_manager.clear_history()

def test_delete_history(history_manager):
    """Test deleting the history file"""
    history_manager.add_entry('add', 1, 2, 3)
    history_manager.delete_history()
    assert not os.path.exists('test_history.csv')
