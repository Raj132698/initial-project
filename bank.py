# import mysql.connector as mysql_bank
#
# conn=mysql_bank.connect(host="hostname",user="root",password="",database="bank")
from random import randint


def open_account():
    name=input("Enter Name: ")

    account_number=randint(10000,100000)

    dob=input("Enter Date of Birth: ")
    phone_number=input("Enter phone number: ")
    address=input("Enter address: ")
    balance=int(input("Enter balance: "))
    if(balance<1000):
        print("Sorry Minimum Balance should be more than 1000")
        main()
    else:
        print("Your Account Number is: ",account_number)
        details=[name,account_number,dob,phone_number,address,balance]
        return details


def withdraw_deposit(details):
    print("""
    What you want to do?
    1. Withdraw 
    2. Deposit
    press other key to go back to Main Menu
    """)
    choice=input("Enter your choice: ")

    if(choice=='1'):
        drawing_amount=int(input("Enter the amount you want to withdraw: "))
        name=input("Enter Name: ")
        if details[0].lower() == name.lower():
            if(details[5]< drawing_amount):
                print("Insufficient Funds | Balance Available : ", details[5])
                return details
            else:
                details[5] -= drawing_amount
                print("Amount has been withdrawn | Updated balance is: ", details[5])
                return details
        else:
            print("Name not found")
            return details

    elif(choice=='2'):
        name = input("Enter Name: ")
        if details[0].lower() == name.lower():
            added_amount=int(input("Enter Amount: "))
            details[5] += added_amount
            print("Account balance has been updated: ", details[5])
            return details

        else:
            print("Name not found")
            return details
    else:
        print("Sorry wrong choice ")
        return details


def balance_enquery(details):
    name = input("Enter Name: ")
    if details[0].lower() == name.lower():
        print("Your balance is:")
        print(details[5])
        key=input("Press any key to go back to main menu")
        if(key):
            return details
    else:
        print("Name not found")
        return details

def display_details(details):
    name = input("Enter Name: ")
    if details[0].lower() == name.lower():
        for i in details:
           print(i, end=" ")
    else:
        print("Name not found")

    return details

#what the heccckkkk!!!!
#hey do it

def welcome():
    print("""
            ********* WELCOME TO ABC BANK ********
            1. Open new Account 
            2. Withdraw amount/ Deposit amount
            3. Balance Enquiry 
            4. Display details
            5. quit
        """)

def main():

    a=True
    details = []
    while(a):
        welcome()
        choice=input("Enter your choice  ")
        if(choice == '1'):
            details=open_account()

        elif(choice =='2'):
            details = withdraw_deposit(details)
        elif(choice =='3'):
            details=balance_enquery(details)
        elif(choice =='4'):
            details=display_details(details)
        elif(choice == '5'):
            print("Thank You _/\_")
            a=False
        else:
            print("Wrong choice")



main()
