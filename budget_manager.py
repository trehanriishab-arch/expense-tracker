import json
import os

BUDGET_FILE = "budget.json"

def load_budget():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r") as f:
            return json.load(f)
    return None

def save_budget(data):
    with open(BUDGET_FILE, "w") as f:
        json.dump(data, f, indent=4)

def setup_budget():
    month = input("Enter month (MM-YYYY): ")

    try:
        monthly_budget = float(input("Enter monthly budget amount: "))
    except:
        print("Invalid budget amount.")
        return

    categories = ["Food", "Travel", "Bills", "Entertainment", "Other"]
    category_limits = {}

    print("Set category limits (enter 0 if not applicable):")
    for cat in categories:
        try:
            category_limits[cat] = float(input(f"{cat} limit: "))
        except:
            category_limits[cat] = 0

    budget_data = {
        "month": month,
        "monthly_budget": monthly_budget,
        "category_limits": category_limits
    }

    save_budget(budget_data)
    print("Budget setup completed successfully.")

def view_budget():
    budget = load_budget()
    if not budget:
        print("No budget set.")
        return

    print("\n--- Budget Overview ---")
    print(f"Month: {budget['month']}")
    print(f"Monthly Budget: ₹{budget['monthly_budget']}")
    print("Category Limits:")
    for cat, amt in budget["category_limits"].items():
        print(f"  {cat}: ₹{amt}")

def check_budget_alerts(expenses, new_expense):
    budget = load_budget()
    if not budget:
        return

    month = budget["month"]
    monthly_limit = budget["monthly_budget"]
    category_limits = budget["category_limits"]

    total_spent = 0
    category_spent = 0

    for exp in expenses:
        if exp["date"][3:] == month:
            total_spent += exp["amount"]
            if exp["category"] == new_expense["category"]:
                category_spent += exp["amount"]

    # Monthly alerts
    if total_spent >= 0.8 * monthly_limit and total_spent < monthly_limit:
        print("⚠ Warning: You have used over 80% of your monthly budget.")
    elif total_spent >= monthly_limit:
        print("❌ Alert: Monthly budget exceeded.")

    # Category alerts
    cat_limit = category_limits.get(new_expense["category"], 0)
    if cat_limit > 0:
        if category_spent >= 0.8 * cat_limit and category_spent < cat_limit:
            print(f"⚠ Warning: {new_expense['category']} budget over 80%.")
        elif category_spent >= cat_limit:
            print(f"❌ Alert: {new_expense['category']} budget exceeded.")
