from functions import *

def show_menu():
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter by Category")
    print("4. Filter by Date")
    print("5. Update an Expense")
    print("6. Delete an Expense")
    print("7. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        amt = float(input("Amount: "))
        cat = input("Category (Food, Travel, etc.): ")
        desc = input("Description: ")
        date = input("Date (YYYY-MM-DD): ")
        add_expense(amt, cat, desc, date)
        print("✅ Expense added!")

    elif choice == '2':
        expenses = view_expenses()
        for exp in expenses:
            print(exp)

    elif choice == '3':
        cat = input("Enter category: ")
        expenses = filter_by_category(cat)
        for exp in expenses:
            print(exp)

    elif choice == '4':
        date = input("Enter date (YYYY-MM-DD): ")
        expenses = filter_by_date(date)
        for exp in expenses:
            print(exp)

    elif choice == '5':
        eid = int(input("Enter expense ID to update: "))
        amt = float(input("New Amount: "))
        cat = input("New Category: ")
        desc = input("New Description: ")
        date = input("New Date (YYYY-MM-DD): ")
        update_expense(eid, amt, cat, desc, date)
        print("🔁 Expense updated.")

    elif choice == '6':
        eid = int(input("Enter expense ID to delete: "))
        delete_expense(eid)
        print("🗑️ Expense deleted.")

    elif choice == '7':
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice, try again.")
