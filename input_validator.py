import re

def get_valid_amount():
    """Get a valid numeric amount."""
    while True:
        try:
            amount = float(input("Enter amount (₹): ").strip())
            if amount <= 0:
                print("Amount must be positive.")
                continue
            return amount
        except ValueError:
            print("Invalid number! Please enter a valid amount.")


def get_valid_category(valid_categories):
    """Get a valid category from the predefined list."""
    print("\nAvailable Categories:", ", ".join(valid_categories))
    while True:
        category = input("Enter category: ").strip().title()
        if category in valid_categories:
            return category
        print("Invalid category! Please choose from the list.")


def get_valid_date():
    """Get a valid date in YYYY-MM-DD format."""
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if re.match(pattern, date):
            return date
        print("Invalid date format! Please use YYYY-MM-DD.")
