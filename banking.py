class User():
    def __init__(self,name, dob, gender, phone_number, address):
        self.name= name
        self.dob= dob
        self.gender= gender
        self.phone_number = phone_number
        self.address =  address

    def show_user_details(self):

        print("User Account Personal Details")
        print(" Name: ",self.name)
        print("Date of Birth: ",self.dob)
        print("Gender: ",self.gender)
        print("Phone Number: ",self.phone_number)
        print("Address: ",self.address)

class Bank(User):
    def __init__ (self,name, age,gender,phone_number,address):
        super().__init__(name,age,gender,phone_number,address)
        self.balance=0

    def deposit(self,amount):
        if self.balance == 0 and amount >= 1000:
            self.balance=self.balance + amount
            print("Account balance has been updated: ", self.balance)
        elif self.balance>0:
            self.balance = self.balance + amount
            print("Account balance has been updated: ", self.balance)
        else:
            print("Minimum Balance is 1000")

    def withdraw(self,amount):
        self.amount = amount
        if self.balance >= self.amount :
            self.balance = self.balance - self.amount
            print("Amount has been withdrawn | Updated balance is: ", self.balance)

        else:
            print("Insufficient Funds | Balance Available : ", self.balance)


    def view_balance(self):
        self.show_user_details()
        print("Your Account balance is : ", self.balance)



def main():
    banking = User()
    a = True
    details = []
    while (a):

        print("""
                    ********* WELCOME TO ABC BANK ********
                    1. Open new Account 
                    2. Withdraw amount/ Deposit amount
                    3. Balance Enquiry 
                    4. Display details
                    5. quit
                """)

        choice = input("Enter your choice  ")
        if (choice == '1'):
            details = open_account()

        elif (choice == '2'):
            details = withdraw_deposit(details)
        elif (choice == '3'):
            details = balance_enquery(details)
        elif (choice == '4'):
            details = display_details(details)
        elif (choice == '5'):
            print("Thank You _/\_")
            a = False
        else:
            print("Wrong choice")



main()