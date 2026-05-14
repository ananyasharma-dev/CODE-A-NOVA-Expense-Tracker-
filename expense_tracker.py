import json
from file_handler import save_expenses, load_expenses
from reports import show_summary

expenses = load_expenses()

def add_expense(expenses):
    desc = input("What did you spend on? ")
    amount = float(input("How much? ₹"))
    expenses.append({"desc": desc, "amount": amount})
    save_expenses(expenses)
    print("Saved!")
    return expenses

while True:
    print("\n1. Add  2. View  3. Summary  4. Exit")
    ch = input("Choice: ")
    if ch == "1":   expenses = add_expense(expenses)
    elif ch == "2": print(expenses)
    elif ch == "3": show_summary(expenses)
    elif ch == "4": break
