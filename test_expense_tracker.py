
import pytest

from expense_tracker import (
    add_expense,
    total_expenses,
    remaining_budget,
    budget_status,
    category_breakdown,
    top_spending_category,
)


def test_add_expense_valid():
    expenses = []

    add_expense(expenses, " food ", 250.5)

    assert expenses[0] == {
        "category": "Food",
        "amount": 250.5,
    }


def test_add_expense_invalid_amount():
    with pytest.raises(ValueError):
        add_expense([], "Food", -50)


def test_total_expenses():
    expenses = [
        {"category": "Food", "amount": 150.25},
        {"category": "Travel", "amount": 349.75},
    ]

    assert total_expenses(expenses) == 500.0


def test_remaining_budget():
    expenses = [
        {"category": "Study", "amount": 1200.0},
    ]

    assert remaining_budget(5000.0, expenses) == 3800.0


def test_budget_status_levels():
    assert budget_status(
        1000,
        [{"category": "Food", "amount": 500}],
    ) == "Under Budget"

    assert budget_status(
        1000,
        [{"category": "Food", "amount": 850}],
    ) == "Near Limit"

    assert budget_status(
        1000,
        [{"category": "Food", "amount": 1200}],
    ) == "Over Budget"


def test_budget_status_invalid_budget():
    with pytest.raises(ValueError):
        budget_status(0, [])


def test_category_breakdown():
    data = [
        {"category": "Food", "amount": 200.0},
        {"category": "Travel", "amount": 150.0},
        {"category": "Food", "amount": 100.0},
    ]

    assert category_breakdown(data) == {
        "Food": 300.0,
        "Travel": 150.0,
    }


def test_top_spending_category():
    data = [
        {"category": "Food", "amount": 200.0},
        {"category": "Travel", "amount": 450.0},
    ]

    assert top_spending_category(data) == ("Travel", 450.0)
