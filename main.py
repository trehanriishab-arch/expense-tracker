import json
import os

FILE_NAME = "expenses.json"
expenses = []

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
    print("4. Exit")

def add_expense():
    name = input("Enter expense name: ")
    try:
        amount = float(input("Enter amount: "))
    except:
        print("Invalid amount.")
        return
    date = input("Enter date (DD-MM-YYYY): ")
    expenses.append({"name": name, "amount": amount, "date": date})
    save_expenses()
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nYour Expenses:")
        total = 0
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp['date']} - {exp['name']}: ₹{exp['amount']}")
            total += exp["amount"]
        print(f"Total: ₹{total}")

def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        index = int(input("Enter expense number to delete: "))
        removed = expenses.pop(index - 1)
        save_expenses()
        print(f"Deleted: {removed['name']} - ₹{removed['amount']}")
    except:
        print("Invalid input.")

# ---- main flow ----
load_expenses()

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 to 4.")
