import csv
import os

FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Amount"])

        writer.writerow([date, category, amount])

    print("Expense Added Successfully!\n")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    print("\n----- Expense List -----")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("\t".join(row))
    print()

def total_expense():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader) # Skip header

        for row in reader:
            total += float(row[2])

    print(f"Total Expense = ₹{total:.2f}\n")

while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Try Again.\n")