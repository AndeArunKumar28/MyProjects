from database import *
from registration import *
from bank import *
def main():
    while True:
        print("---Banking user---")
        print("1> signup")
        print("2> login")
        print("3> exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            sign_up()
        elif choice==2:
            login()
            temp=Bank(username=user)
            if temp:
                while True:
                    print("---Banking Menu--")
                    print("1> Deposit")
                    print("2> Withdraw")
                    print("3> Balance_enquiry")
                    print("4> Exit")
                    ch=int(input("Choose yor service: "))
                    if ch==1:
                        b1.deposit()
                    elif ch==2:
                        b1.withdraw()
                    elif ch==3:
                        b1.balance_enquiry()
                    elif ch==4:
                        print("Thanks for using our services")
                        break
                    else:
                        print("invalid choice try again")
        elif choice==3:
            print("Thankyou and welcome")
            break
        else:
            print("Invalid option please try again.")

main()
