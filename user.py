from database import *

class user:
    def __init__(self,username,email,phone,password,balance,deposit,withdraw):
        self.username=username
        self.email=email
        self.phone=phone
        self.password=password
        self.balance=balance
        self.deposit=deposit
        self.withdraw=withdraw

    def user(self):
        (f"INSERT INTO user VALUES ('{self.username}','{self.email}','{self.phone}',{self.password}','{self.balance}','{self.deposit}','{self.withdraw}')")