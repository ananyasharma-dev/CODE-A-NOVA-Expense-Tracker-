def show_summary(expenses):
    if not expenses:
        print("No data yet.")
        return
    total = sum(e["amount"] for e in expenses)
    avg   = total / len(expenses)
    print(f"\nTotal spent : ₹{total:.2f}")
    print(f"Average     : ₹{avg:.2f}")
    print(f"No. entries : {len(expenses)}")
