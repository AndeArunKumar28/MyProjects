from database import *
from registration import *

class Bank():

    def __init__(self,username,balance=0):
        self.username=username
        self.balance=balance

    def balance_enquiry(self):
        print(f"{self.username} current balance is {self.balance}")

        
    def deposit(self):
        amount=int(input("Enter your amount: "))
        if amount>0:
            self.balance+=amount
            print(f"Deposited Amount: {amount} updated balance is {self.balance}")
        else:
            print("Depositing amount must be positive")

    def withdraw(self):
        amount=int(input("Enter your amount: "))
        if 0<amount<self.balance:
            self.balance-=amount
            print(f"Withdrawn Amount: {amount} updated balance is {self.balance}")
        else:
            print("Insufficient funds please deposit amount")

b1=Bank(username=user)
