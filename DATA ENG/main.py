#Assessment2_ExpenseTracker
# main.py
#README.md

expenses = [
    {"name": "Transport", "amount": 3000},
    {"name": "Food", "amount": 4500},
    {"name": "Internet", "amount": 12000},
    {"name": "Book", "amount": 7000},
    {"name": "Data", "amount": 5000}
]  

def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total
print("Daily Expense Report")
print("-------------------")

high_expense_count = 0

for expense in expenses:
    if expense["amount"] > 10000:
        status = "High Expense"
        high_expense_count += 1
    else:
        status = "Normal Expense"

    print(f"{expense['name']}: {expense['amount']} - {status}")

    total_spent = calculate_total(expenses)

print("\nTotal Amount Spent:", total_spent)
print("High Expenses:", high_expense_count)

# Expense List
expenses = [
    {"name": "Transport", "amount": 3000},
    {"name": "Food", "amount": 4500},
    {"name": "Internet", "amount": 12000},
    {"name": "Books", "amount": 7000},
    {"name": "Data", "amount": 15000}
]


# Function to calculate total expenses
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


print("Daily Expense Report")
print("-------------------")

high_expense_count = 0

for expense in expenses:

    if expense["amount"] > 10000:
        status = "High Expense"
        high_expense_count += 1
    else:
        status = "Normal Expense"

    print(f"{expense['name']}: {expense['amount']} - {status}")

total_spent = calculate_total(expenses)

print("\nTotal Amount Spent:", total_spent)
print("High Expenses:", high_expense_count)
