### Feature 2: Add Transactions

def add(expense):

    # ID = int(input("Enter your id :"))
    # Type = input("enter your expense type :")
    # Amount = int(input("enter your amount :"))
    # category = input("enter your category :")
    # date = input("enter your date :")

    exp = {
        "Transaction_id": int(input("Enter your id :")),
        "expense_type": input("enter your expense type :"),
        "exp_amount": int(input("enter your amount :")),
        "exp_Category": input("enter your category :"),
        "exp_date": input("enter your date :"),
    }
    expense.append(exp)
    print(" ")



