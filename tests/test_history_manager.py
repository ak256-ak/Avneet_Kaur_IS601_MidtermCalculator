import pytest
import os
from calculator.history_manager import HistoryManagerFacade

@pytest.fixture
def history_manager():
    return HistoryManagerFacade('test_history.csv')

def test_add_entry(history_manager):
    history_manager.add_entry('add', 3, 2, 5)
    df = history_manager.load_history()
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
