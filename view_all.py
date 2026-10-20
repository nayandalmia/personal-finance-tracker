def view(expense):
    for i in expense:
        print(" ")
        print("My transaction id is :", i["Transaction_id"])
        print("Transaction type is : ", i["expense_type"])
        print("Transaction amount is :", i["exp_amount"])
        print("the category of expense is :", i["exp_Category"])
        print("----------------------------------------------")
        print(" ")