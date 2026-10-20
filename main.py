from add import add
from search import search,greet
from view_all import view
from update import update
from delete import delete
from financial_report import report

 # default data
expense = [
    {
        "Transaction_id": 1,
        "expense_type": 'Income',
        "exp_amount": 500,
        "exp_Category": 'rent',
        "exp_date": '13/11/2026',
    },
        {
        "Transaction_id": 2,
        "expense_type": 'Income',
        "exp_amount": 598,
        "exp_Category": 'salary',
        "exp_date": '13/11/2026',
    },
]

while True:
   
    print("Personal Finance Tracker")
    print("Please choose from the following:  ")
    print("1. Add All Transactions \t 2. View All Transactions")
    print("3. Search Transactions  \t 4. Edit a Transaction ")
    print("5. Delete a Transaction \t 6. View Financial Summaries")
    print("7. Exit Application")
    k = input("Please write the number you want to choose: ")
    if k == "1":
        add(expense=expense)
    elif k == "2":
        view(expense=expense)
    elif k == "3":
        search(expense=expense)
    elif k == "4":
        update(expense=expense) 
    elif k == "5":
       delete(expense = expense)
    elif k == "6":
        report(expense=expense) 
    elif k == "7":
        print("exit")
        break
    else:
        print("Please enter a valid number: ")