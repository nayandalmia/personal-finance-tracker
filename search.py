### Feature 3: View and Search Transactions

def search(expense):
    print("Search and filter")
    print("Please select from the following: ")
    print("1. Type of expense \t 2. search category")
    print("3. Enter the date  \t 4. Minimum and Maximum amount")

    choice = input("enter your choice:")

    if choice == "1":
        se_ty = input("Income, Expense: ")
       
        for i in expense:
            if i["expense_type"] == se_ty:
                print("----------------------------------------------")
                print(" ")
                print("My transaction id is :", i["Transaction_id"])
                print("Transaction type is : ", i["expense_type"])
                print("Transaction amount is :", i["exp_amount"])
                print("the category of expense is :", i["exp_Category"])
                print("----------------------------------------------")
                print(" ")
        

def greet():
    print("helllo greeting from search")
      
            
       



