expenses = []

def show_menu():
    print("\n--- Student Expense Tracker ---")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((name, amount))
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\nYour Expenses:")
            total = 0
            for name, amount in expenses:
                print(f"{name}: ₹{amount}")
                total += amount
            print(f"Total: ₹{total}")

    elif choice == "3":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        