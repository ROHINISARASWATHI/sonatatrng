from classaccount import Account


def withdraw(balance, amount):
    if (balance < amount):
        raise lowbalanceexception("There is no sufficient balance in your account")
    balance = balance - amount

