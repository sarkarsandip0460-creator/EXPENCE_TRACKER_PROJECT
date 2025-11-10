from expense_app.expense import Expense
from expense_app.file_handler import read_expenses, write_expenses
from expense_app.input_validator import get_valid_amount, get_valid_category, get_valid_date
from expense_app.summary import summarize_by_category

EXPENSES_FILE = "data/expenses.txt"

def main_menu():
    print("\n==============================")
    print("       EXPENSE TRACKER        ")
    print("==============================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary by Category")
    print("4. Delete an Expense")
    print("5. Exit")
    print("==============================")

def add_expense(expenses):
    amount = get_valid_amount()
    category = get_valid_category(Expense.CATEGORIES)
    date = get_valid_date()

    new_expense = Expense(amount, category, date)
    expenses.append(new_expense)
    write_expenses(EXPENSES_FILE, expenses)
    print("✅ Expense added successfully!")
def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    print("\n--- All Expenses ---")
    print(f"{'Date':<12} | {'Category':<15} | {'Amount'}")
    print("-" * 40)
    for exp in expenses:
        print(exp)

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        index = int(input("\nEnter expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            write_expenses(EXPENSES_FILE, expenses)
            print(f"🗑 Deleted: {removed.category} - ₹{removed.amount:.2f}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")
def run_app():
    print("🚀 Expense Tracker App Started!")
    expenses = read_expenses(EXPENSES_FILE)
    while True:
        main_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            summarize_by_category(expenses)
        elif choice == '4':
            delete_expense(expenses)
        elif choice == '5':
            print("👋 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
        run_app()
