from collections import defaultdict

def summarize_by_category(expenses):
    """Summarize total spending per category."""
    if not expenses:
        print("\nNo expenses to summarize.\n")
        return

    summary = defaultdict(float)
    for exp in expenses:
        summary[exp.category] += exp.amount

    print("\n--- Expense Summary by Category ---")
    print(f"{'Category':<15}{'Total Amount (₹)'}")
    print("-" * 35)

    for cat, total in summary.items():
        print(f"{cat:<15}₹{total:.2f}")

