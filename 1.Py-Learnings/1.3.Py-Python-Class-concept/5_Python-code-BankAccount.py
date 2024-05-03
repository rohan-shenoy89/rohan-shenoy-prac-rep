#Create a Python class called BankAccount. It should have attributes for the account holder's name and balance. Include methods to deposit and withdraw money from the account.

class BankAccount():
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance

    def credit(self,amount):
        self.balance += amount
        return f"Amount deposited ${amount}. Total Balance - ${self.balance}"

    def debit(self,amount):
        if self.balance > amount:
            self.balance -= amount
            return f"Withdrawal of ${amount} was done. Total balance - ${self.balance}"
        else:
            return "Insufficient Balance"

user1 = BankAccount("Rohan")
print(user1.credit(300))
print(user1.debit(400))
