def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.\n")
        return

    category = input("Enter category: ")

    with open("expenses.txt", "a") as file:
        file.write(str(amount) + "," + category + "\n")

    print("Expense added successfully!\n")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()

            if not expenses:
                print("No expenses recorded.\n")
                return

            print("\nYour Expenses:")
            for expense in expenses:
                amount, category = expense.strip().split(",")
                print(f"Amount: ₹{amount} | Category: {category}")

            print()

    except FileNotFoundError:
        print("No expenses file found.\n")


def main():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()