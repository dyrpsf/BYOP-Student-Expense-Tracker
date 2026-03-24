import json
import os
from datetime import datetime

DATA_FILE = "data.json"


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    print("\n--- Add New Expense ---")
    title = input("Enter expense title: ").strip()
    category = input("Enter category (Food/Travel/Shopping/Study/etc): ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

    if date_input == "":
        date_input = datetime.today().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

    expense = {
        "title": title,
        "category": category,
        "amount": amount,
        "date": date_input
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n--- All Expenses ---")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. Title: {expense['title']}, "
            f"Category: {expense['category']}, "
            f"Amount: ₹{expense['amount']}, "
            f"Date: {expense['date']}"
        )


def total_expense():
    expenses = load_expenses()
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expense: ₹{total}")


def filter_by_category():
    expenses = load_expenses()
    category = input("\nEnter category to filter: ").strip().lower()

    filtered = [
        expense for expense in expenses
        if expense["category"].lower() == category
    ]

    if not filtered:
        print("No expenses found in this category.")
        return

    print(f"\n--- Expenses in Category: {category} ---")
    for index, expense in enumerate(filtered, start=1):
        print(
            f"{index}. Title: {expense['title']}, "
            f"Amount: ₹{expense['amount']}, "
            f"Date: {expense['date']}"
        )


def monthly_summary():
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    summary = {}

    for expense in expenses:
        month = expense["date"][:7]  # YYYY-MM
        summary[month] = summary.get(month, 0) + expense["amount"]

    print("\n--- Monthly Summary ---")
    for month, total in summary.items():
        print(f"{month}: ₹{total}")


def delete_expense():
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses available to delete.")
        return

    view_expenses()

    try:
        index = int(input("\nEnter expense number to delete: "))
        if 1 <= index <= len(expenses):
            removed = expenses.pop(index - 1)
            save_expenses(expenses)
            print(f"Deleted expense: {removed['title']}")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")