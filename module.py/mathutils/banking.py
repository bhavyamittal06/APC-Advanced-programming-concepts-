def create_account(name):
    print("Account Created",name)

# banking/transaction.py
def deposit(bal,amt):
    return bal+amt

# banking/loan.py
def loan_interest(p,r,t):
    return (p*r*t)/100
