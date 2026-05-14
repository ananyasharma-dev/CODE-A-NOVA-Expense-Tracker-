import json, os

FILE = "expenses.json"

def save_expenses(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_expenses():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)
