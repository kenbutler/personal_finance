"""
Transaction
"""
from datetime import date


class Transaction:

    def __init__(self, starting_value: float, change: float, date_of_transaction: date, description: str = ""):
        self.date: date = date_of_transaction
        self.starting_value: float = starting_value
        self.change: float = change
        self.description: str = description
