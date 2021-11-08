# import mysql.connector as mysql_bank
#
# conn=mysql_bank.connect(host="hostname",user="root",password="",database="bank")



def open_account():
    name=input("Enter Name: ")
    account_number=input("Enter Account Number: ")
    dob=input("Enter Date of Birth: ")
    phone_number=input("Enter phone number: ")
    address=input("Enter address: ")
    balance=int(input("Enter balance"))
    if(balance<1000):
        print("Sorry Minimum Balance should be more than 1000")
        main()
    else:
        data=(name,account_number,dob,phone_number,address,balance)
        sql='insert into account values(%s,%s,%s,%s,%s,%s)'
        connection=conn.cursor()
        connection.execute(sql,data)
        connection.commit()
        print("Data Entered Successfully")
        main()


def withdraw_deposit():
    print("""
    What you want to do?
    1. Withdraw 
    2. Deposit
    """)
    choice=input("Enter your choice: ")

    if(choice=='1'):
        drawing_amount=int(input("Enter the amount you want to withdraw: "))
        account_number=input("Enter Account Number: ")
        query="select balance from account where account_number= %s"
        data=(account_number,)
        connections=conn.cursor()
        connections.execute(query,data)
        amounts=connections.fetchone()
        if(amounts[0] < drawing_amount):
            print("Sorry low balance transaction failed")
            main()
        else:
            withdrawing_amount=amounts[0]-drawing_amount
            sql_querys="update amount set balance=%s where account_number= %s"
            entry=(withdrawing_amount,account_number)
            connections.execute(sql_querys,entry)
            conn.commit()
            main()

    elif(choice=='2'):
        added_amount=int(input("Enter Amount: "))
        account_number=input("Enter your Account Number: ")
        added_query="select balance from account where account_number= %s"
        data=(account_number,)
        connection=conn.cursor()
        connection.execute(added_query,data)
        amounts=connection.fetchone()
        adding_amount=amounts[0]+added_amount
        sql_query="update amount set balance= %s where account_number= %s"
        data_entry=(adding_amount,account_number)
        connection.execute(sql_query,data_entry)
        conn.commit()
        main()
    else:
        print("Sorry wrong choice ")
        main()


def balance_enquery():
    account_number = input("Enter Account Number: ")
    query = "select balance from account where account_number= %s"
    data = (account_number,)
    connections = conn.cursor()
    connections.execute(query, data)
    amounts = connections.fetchone()
    while(True):
        print("Your balance is:")
        print(amounts[0])
        key=input("Press any key to go back to main menu")
        if(key):
            main()


def display_details():
    account_number=input("Enter Account Number: ")
    account_query="select * from account where account_number = %s"
    data=(account_number,)
    connection=conn.cursor()
    connection.execute(account_query,data)
    details=connection.fetchone()
    for i in details:
        print(i,end="  ")
    main()



def main():
    print("""
        ********* WELCOME TO ABC BANK ********
        1. Open new Account 
        2. Withdraw amount/ Deposit amount
        3. Balance Enquiry 
        4. Display details
        5. quit
    """)
    while(True):
        choice=input("Enter your choice  ")
        if(choice == '1'):
            open_account()
        elif(choice =='2'):
            withdraw_deposit()
        elif(choice =='3'):
            balance_enquery()
        elif(choice =='4'):
            display_details()
        elif(choice == '5'):
            print("Thank You _/\_")
            break
        else:
            print("wrong choice")


main()