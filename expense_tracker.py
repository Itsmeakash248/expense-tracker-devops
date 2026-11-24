
# expense_tracker.py


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


def category_breakdown(expenses):
    summary = {}

    for item in expenses:
        cat = item["category"]
        summary[cat] = round(
            summary.get(cat, 0.0) + item["amount"], 2
        )

    return summary


def top_spending_category(expenses):
    summary = category_breakdown(expenses)

    if not summary:
        return None

    top_cat = max(summary, key=summary.get)

    return (top_cat, summary[top_cat])


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

        while True:
            try:
                amt = float(input("Amount (INR) : "))

                if amt <= 0:
                    print(
                        "Invalid amount! Please enter an amount "
                        "greater than zero."
                    )
                    continue

                add_expense(expenses, cat, amt)
                break

            except ValueError:
                print("Invalid input! Please enter a valid numeric amount.")

    print("\n" + "=" * 54)
    print(" EXPENSE SUMMARY")
    print("=" * 54)

    print(f"Total Spent : INR {total_expenses(expenses):.2f}")
    print(
        f"Remaining Balance : INR "
        f"{remaining_budget(budget, expenses):.2f}"
    )
    print(f"Budget Status : {budget_status(budget, expenses)}")

    print("\nCategory Breakdown:")

    for cat, amt in category_breakdown(expenses).items():
        print(f" - {cat:<16}: INR {amt:.2f}")

    top_cat = top_spending_category(expenses)

    if top_cat:
        print(
            f"\nTop Category : {top_cat[0]} "
            f"(INR {top_cat[1]:.2f})"
        )

    print("=" * 54)


if __name__ == "__main__":
    main()
