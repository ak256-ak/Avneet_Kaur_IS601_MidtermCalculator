import pandas as pd
import os
import logging

class HistoryManagerFacade:
    """Facade for managing calculation history"""

    def __init__(self, filepath='calculator_history.csv'):
        self.filepath = filepath
        self._initialize_file()

    def _initialize_file(self):
        """Initialize the history file if it doesn't exist"""
        if not os.path.exists(self.filepath):
            try:
                df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
                df.to_csv(self.filepath, index=False)
                logging.info("Initialized history file.")
            except Exception as e:
                logging.error(f"Failed to initialize history file: {e}")

    def add_entry(self, operation, operand1, operand2, result):
        """Add a new entry to the history file"""
        try:
            df = pd.DataFrame([[operation, operand1, operand2, result]], 
                              columns=['Operation', 'Operand1', 'Operand2', 'Result'])
            df.to_csv(self.filepath, mode='a', header=False, index=False)
            logging.info(f"Added history entry: {operation}, {operand1}, {operand2}, {result}")
        except Exception as e:
            logging.error(f"Failed to add history entry: {e}")

    def load_history(self):
        """Load the calculation history"""
        try:
            if os.path.exists(self.filepath):
                df = pd.read_csv(self.filepath)
                return df
            else:
                logging.warning("No history file found.")
                return pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        except Exception as e:
            logging.error(f"Failed to load history: {e}")
            return pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

    def clear_history(self):
        """Clear all calculation history"""
        try:
            df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
            df.to_csv(self.filepath, index=False)
            logging.info("Cleared history file.")
        except Exception as e:
            logging.error(f"Failed to clear history: {e}")

    def save_history(self):
        """Save the current history"""
        try:
            df = self.load_history()
            df.to_csv(self.filepath, index=False)
            logging.info("History saved.")
        except Exception as e:
            logging.error(f"Failed to save history: {e}")

    def delete_history(self):
        """Delete the history file"""
        try:
            if os.path.exists(self.filepath):
                os.remove(self.filepath)
                logging.info("History file deleted.")
            else:
                logging.warning("No history file found to delete.")
        except Exception as e:
            logging.error(f"Failed to delete history: {e}")
