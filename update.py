
### Feature 4: Edit and Delete Transactions


def update(expense):
    user = int(input("enter your id :"))

    for i in expense:
        if i["Transaction_id"] == user:
            print("Transaction_id found")
            print("My transaction id is :", i["Transaction_id"])
            print("Transaction type is : ", i["expense_type"])
            print("Transaction amount is :", i["exp_amount"])
            print("the category of expense is :", i["exp_Category"])

            new = int(input("enter your new amount :"))
            i["exp_amount"] = new
            print("transaction succesfully updated")
        else:
            print("no transaction found ")


    

            



