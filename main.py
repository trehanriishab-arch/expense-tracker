from expense_manager import (
    load_expenses,
    add_expense,
    view_expenses,
    delete_expense,
    monthly_summary
)

def show_menu():
    print("\n--- Student Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Monthly summary")
    print("5. Exit")

load_expenses()
print("Welcome to Student Expense Tracker")

while True:
    show_menu()
    choice = input("Enter choice (1-5): ").strip()

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
        print("Invalid choice. Enter a number from 1 to 5.")
