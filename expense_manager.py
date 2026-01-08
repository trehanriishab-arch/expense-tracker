import json
import os
from datetime import datetime
from budget_manager import check_budget_alerts

FILE_NAME = "expenses.json"
CATEGORIES = ["Food", "Travel", "Bills", "Entertainment", "Other"]
expenses = []

def load_expenses():
    global expenses
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            expenses = json.load(f)

def save_expenses():
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def show_categories():
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}. {cat}")

def get_float(prompt):
    try:
        return float(input(prompt))
    except:
        print("Invalid number.")
        return None

def get_valid_date(prompt):
    date_str = input(prompt)
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return date_str
    except:
        print("Invalid date format. Use DD-MM-YYYY.")
        return None

def add_expense():
    name = input("Enter expense name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    amount = get_float("Enter amount: ")
    if amount is None or amount <= 0:
        print("Amount must be positive.")
        return

    show_categories()
    try:
        category = CATEGORIES[int(input("Enter category number: ")) - 1]
    except:
        print("Invalid category.")
        return

    date = get_valid_date("Enter date (DD-MM-YYYY): ")
    if not date:
        return

    new_expense = {
        "name": name,
        "amount": amount,
        "date": date,
        "category": category
    }

    expenses.append(new_expense)
    save_expenses()

    check_budget_alerts(expenses, new_expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = 0
    print("\nYour Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['name']} : ₹{exp['amount']}")
        total += exp["amount"]

    print("-" * 30)
    print(f"Total Amount: ₹{total}")
    print("-" * 30)

def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        idx = int(input("Enter expense number to delete: ")) - 1
        if idx < 0 or idx >= len(expenses):
            raise ValueError
        removed = expenses.pop(idx)
        save_expenses()
        print(f"Deleted: {removed['name']}")
    except:
        print("Invalid selection.")

def monthly_summary():
    month = input("Enter month and year (MM-YYYY): ")
    try:
        datetime.strptime("01-" + month, "%d-%m-%Y")
    except:
        print("Invalid month format. Use MM-YYYY.")
        return

    summary = {}
    total = 0

    for exp in expenses:
        if exp["date"][3:] == month:
            summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]
            total += exp["amount"]

    if total == 0:
        print("No expenses found for this month.")
        return

    print("\n" + "-" * 30)
    print(f"Summary for {month}")
    print("-" * 30)
    for cat, amt in summary.items():
        print(f"{cat:<15}: ₹{amt}")
    print("-" * 30)
    print(f"Total Amount   : ₹{total}")
    print("-" * 30)