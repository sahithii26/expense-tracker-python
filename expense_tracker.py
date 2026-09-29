expenses = []


def add_expense():
    print("\n--- Add Expense ---")

    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense added successfully!")


def show_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses available.")
        return

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. {expense['name']} - "
            f"₹{expense['amount']:.2f} - "
            f"{expense['category']}"
        )


def show_total():
    print("\n--- Total Spending ---")

    if not expenses:
        print("No expenses available.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total spending: ₹{total:.2f}")


def delete_expense():
    if not expenses:
        print("\nNo expenses to delete.")
        return

    show_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            print(f"Deleted: {deleted['name']}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("\nThank you for using Expense Tracker!")
        break

    else:
        print("\nInvalid choice. Please select 1-5.")