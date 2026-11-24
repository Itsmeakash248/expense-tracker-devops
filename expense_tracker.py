
# expense_tracker.py (Initial Version)


def add_expense(expenses, category, amount):
    if amount <= 0:
        raise ValueError("Expense amount must be greater than zero.")

    clean_category = category.strip().title() or "General"
    expenses.append({
        "category": clean_category,
        "amount": float(amount)
    })

    return expenses


def total_expenses(expenses):
    return round(sum(item["amount"] for item in expenses), 2)


def remaining_budget(budget, expenses):
    return round(float(budget) - total_expenses(expenses), 2)


def budget_status(budget, expenses):
    if budget <= 0:
        raise ValueError("Budget must be greater than zero.")

    ratio = total_expenses(expenses) / float(budget)

    if ratio > 1.0:
        return "Over Budget"
    elif ratio >= 0.8:
        return "Near Limit"

    return "Under Budget"


def main():
    print("=" * 54)
    print(" PERSONAL EXPENSE & BUDGET TRACKER")
    print("=" * 54)

    budget = float(input("Enter Monthly Budget (INR) : "))
    count = int(input("Enter number of expenses : "))

    expenses = []

    for i in range(1, count + 1):
        print(f"\n--- Expense {i} ---")

        cat = input("Category (Food/Travel/Study): ")
        amt = float(input("Amount (INR) : "))

        add_expense(expenses, cat, amt)

    print("\n" + "=" * 54)
    print(f"Total Spent : INR {total_expenses(expenses):.2f}")
    print(f"Remaining Balance : INR {remaining_budget(budget, expenses):.2f}")
    print(f"Budget Status : {budget_status(budget, expenses)}")
    print("=" * 54)


if __name__ == "__main__":
    main()
