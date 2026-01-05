import json
import os

FILE_NAME = "expenses.json"
expenses = []

CATEGORIES = ["Food", "Travel", "Bills", "Entertainment", "Other"]

def load_expenses():
    global expenses
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            expenses = json.load(f)

def save_expenses():
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def show_menu():
    print("\n--- Student Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Monthly summary")
    print("5. Exit")

def show_categories():
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}. {cat}")

def add_expense():
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter amount: "))
    except:
        print("Invalid amount.")
        return

    show_categories()
    try:
        category = CATEGORIES[int(input("Enter category number: ")) - 1]
    except:
        print("Invalid category.")
        return

    date = input("Enter date (DD-MM-YYYY): ")

    expenses.append({
        "name": name,
        "amount": amount,
        "date": date,
        "category": category
    })

    save_expenses()
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = 0
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['name']} : ₹{exp['amount']}")
        total += exp["amount"]
    print(f"Total: ₹{total}")

def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        removed = expenses.pop(int(input("Enter expense number to delete: ")) - 1)
        save_expenses()
        print(f"Deleted: {removed['name']}")
    except:
        print("Invalid input.")

def monthly_summary():
    month = input("Enter month and year (MM-YYYY): ")

    summary = {}
    total = 0

    for exp in expenses:
        if exp["date"][3:] == month:
            summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]
            total += exp["amount"]

    if total == 0:
        print("No expenses found for this month.")
        return

    print(f"\nSummary for {month}")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")
    print(f"Total: ₹{total}")

# ---- main flow ----
load_expenses()

while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        monthly_summary()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice.")
