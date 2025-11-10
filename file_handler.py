from expense_app.expense import Expense
def read_expenses(filename):
    """Load all expenses from a text file."""
    expenses = []
    try:
        with open(filename, "r") as f:
            for line in f:
                expenses.append(Expense.from_line(line))
    except FileNotFoundError:
        pass  # No file yet — return empty list
    return expenses


def write_expenses(filename, expenses):
    """Save all expenses to a text file."""
    with open(filename, "w") as f:
        for exp in expenses:
            f.write(exp.to_line())
