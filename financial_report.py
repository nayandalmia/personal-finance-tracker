# ### Feature 5: Financial Reports

# Generate the following reports:

# - Total income
# - Total expenses
# - Current balance
# 
# - Highest-value expense
# - Average expense


# Use the following formula:

# Balance = Total Income − Total Expenses

def report(expense):

    user = input("enter your expense type:")

    total_income = 0
    total_expense = 0

    for i in expense:
        if  "Income" == user:
            total_income += i["exp_amount"]
        elif  "Expense" == user:
            total_expense += i["exp_amount"]
        else:
            print("No transaction found :") 

    current_balance  = total_income - total_expense
    print("Total Income: ", total_income)
    print("Total Expense: ", total_expense)
    print("My current balance is :", current_balance)


    max_amount = max(x["exp_amount"] for x in expense)
    print("Highest expense recorded is :" , max_amount)
    print(" ")
        





        
        






    

