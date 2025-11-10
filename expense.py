import re

class Expense:
    """Represents a single expense record."""
    
    CATEGORIES = ("Food", "Transport", "Utilities", "Entertainment", "Other")

    def _init_(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def _str_(self):
        return f"{self.date} | {self.category:<15} | ₹{self.amount:.2f}"

    def to_line(self):
        """Convert Expense to string format for file storage."""
        return f"{self.amount},{self.category},{self.date}\n"

    @staticmethod
    def from_line(line):
        """Create an Expense object from a saved line."""
        amount, category, date = line.strip().split(",")
        return Expense(float(amount), category, date)
