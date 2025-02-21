from database import *
from user import *

user={}

def sign_up():
    print("welcome to the mybank")
    username=input("Enter your username: ")
    if username in user:
        print("username already exists try new one.")
        return
    email=input("enter your email: ")
    mobile=input("Enter your phone number: ")
    password=input("Enter your password: ")
    user[username]=password
    print(f"{username} signup was succesfull please login")

def login():
    print("Kindly login with your credentials")
    username=input("Enter your username: ")
    if username not in user:
        print("user not found kindly check and please signup")
        return
    password=input("Enter your password: ")
    if user[username]==password:
        print(f"{username} welcome to bank your login was successfull")
    else:
        print("invalid password please try again")
    