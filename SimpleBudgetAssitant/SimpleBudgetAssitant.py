def menu():
    print("\nMenu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View All Transactions")
    print("5. View Total by Expense Category ")
    print("6. Exit")
    return int(input("Choose an option from 1-6:"))

def add_income():
    income_amount=float(input("Amount?"))
    income_source = input("Source?")
    income_transaction={"Type": "Income","Amount":income_amount, "Source": income_source}
    transactions.append(income_transaction)

def add_expense():
    expense_amount=float(input("Amount?"))
    expense_category=input("Category?")
    expense_description=input("Description:")
    expense_transaction={"Type": "Expense", "Amount":expense_amount, "Category":expense_category, "Description":expense_description}
    transactions.append(expense_transaction)

def balance():
    if not transactions:
        print("No Balance")

    income_amount = 0
    expense_amount = 0
    for transaction in transactions:
        if transaction["Type"] == "Income":
            income_amount += transaction["Amount"]
        else:
            expense_amount += transaction["Amount"]

    current_balance = income_amount - expense_amount
    print("Balance: $" , current_balance)

def view_transactions():
    if not transactions:
        print("No transactions recorded")
        return
    
    for transaction in transactions:
        if transaction["Type"] == "Income":
            print(f"{transaction['Type']}: ${transaction['Amount']} from {transaction['Source']}")
        else:
            print(f"{transaction['Type']}: ${transaction['Amount']} on {transaction['Category']} ({transaction['Description']})")
            
def total_expenses_category():
    expense_categories = {}
    for transaction in transactions:
        if transaction["Type"] == "Expense":
            category = transaction["Category"]
            amount = transaction["Amount"]

            if category in expense_categories:
                expense_categories[category] += amount
            else:
                expense_categories[category] = amount
    print("\nTotal Expenses by Category:")
    for category, total in expense_categories.items():
        print(f"-{category}: ${total}")


transactions = []

while True:
    choice = menu()

    match choice:
        case 1:
            add_income()

        case 2:
            add_expense()

        case 3:
            balance()

        case 4:
            view_transactions()

        case 5:
            total_expenses_category()

        case 6:
            print("Goodbye!")
            break
        case _:
            print("Invalid Choice. Select an option from 1-6")
