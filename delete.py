

def delete(expense):
    user  = int(input("enter your id :"))
    for i in expense:
        if  i["Transaction_id"] == user:
            expense.remove(i)
            print("Transaction removed :")
       

 