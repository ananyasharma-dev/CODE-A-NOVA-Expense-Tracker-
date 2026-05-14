from file_handler import save_expenses, load_expenses
from reports import show_summary

expenses = load_expenses()

def add_expense():
    desc     = input("What did you spend on? ")
    amount   = float(input("How much? Rs."))
    category = input("Category (Food/Travel/Other): ")
    expenses.append({"desc": desc, "amount": amount, "category": category})
    save_expenses(expenses)
    print("Expense saved!")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
        return
    print("\n--- Your Expenses ---")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['desc']} | Rs.{e['amount']} | {e['category']}")

# Main menu
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if   choice == "1": add_expense()
    elif choice == "2": view_expenses()
    elif choice == "3": show_summary(expenses)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
