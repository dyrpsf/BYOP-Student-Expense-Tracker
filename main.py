from expense_manager import (
    add_expense,
    view_expenses,
    total_expense,
    filter_by_category,
    monthly_summary,
    delete_expense
)


def show_menu():
    print("\n========== Student Expense Tracker ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Filter by Category")
    print("5. Monthly Summary")
    print("6. Delete Expense")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 7.")


if __name__ == "__main__":
    main()
