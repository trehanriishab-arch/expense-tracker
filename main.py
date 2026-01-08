from expense_manager import (
    load_expenses,
    add_expense,
    view_expenses,
    delete_expense,
    monthly_summary
)

from budget_manager import (
    setup_budget,
    view_budget
)

def show_menu():
    print("\n--- Student Budget Assistant ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Monthly summary")
    print("5. Setup / Update budget")
    print("6. View budget")
    print("7. Exit")

# Load existing expenses at startup
load_expenses()
print("Welcome to Student Budget Assistant")

while True:
    show_menu()
    choice = input("Enter choice (1-7): ").strip()

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        monthly_summary()

    elif choice == "5":
        setup_budget()

    elif choice == "6":
        view_budget()

    elif choice == "7":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
