"""
Reservoirs of money
"""
from datetime import date
from enum import Enum


class Frequency(Enum):
    FIXED = 0,
    MONTHLY = 1,
    YEARLY = 2


class Reservoir:

    def __init__(self,
                 name: str, category: str, essential: bool = False,
                 initial_value: float = 0.0,
                 savings_rate: float = 0.0, savings_rate_type: Frequency = Frequency.FIXED,
                 limit: float = 0.0):
        self.name: str = name
        self.category: str = category
        self.essential: bool = essential  # Useful for computing cost of living for paycheck
        self.value: float = initial_value
        self.savings_rate: float = savings_rate
        self.savings_rate_type: Frequency = savings_rate_type
        self.limit: float = limit
        self.last_changed: date = date.today()
        self.history: list = []  # No history upon initial creation
        self.history_limit: int = 10

    # TODO: Add getters and setters

    def add_to_ledger(self):
        return  # TODO

    def set_value(self, change: float, date_of_change: date = date.today()):
        change = round(change, 2)
        if self.value + change < 0:
            raise IOError("Input value (%d) will reduce current value (%d) to a negative number. Not permissible.",
                              change, self.value)
        # Not applying conditional check against upper limit here, as it's only a limit in regards to paycheck
        # allocation
        self.value += change
        self.last_changed = date_of_change
