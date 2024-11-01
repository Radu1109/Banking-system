# Welcome to my BANK
import account_managment
from Account import Account
from database import get_user_info
from database import connect_to_database
from account_managment import *
import pymysql

conn = connect_to_database()
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS customers(
               id_customer INT AUTO_INCREMENT PRIMARY KEY,
               first_name VARCHAR(15),
               last_name VARCHAR(15),
               email VARCHAR(50),
               username VARCHAR(20), 
               `pin` VARCHAR(4),
               money DECIMAL(6,2)
               )
''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS transactions(
               id_transaction INT AUTO_INCREMENT PRIMARY KEY,
               date_of_transaction TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
               amount DECIMAL(4,2),
               id_customer INT
               )
''')
def main():
    print("******************")
    print("Welcome to my Bank!")
    print("******************\n")
    user_input = str(input("Do you have an account? \n"
                       "Y/N\n").upper())
    while True:
        if user_input == "N":
            new_account = Account()
            print("Your account information is : \n")
            new_account.display_account()
            new_account.insert_account_into_db(new_account)
            username = new_account.username
            break
        elif user_input == "Y":
            username = input("Enter your username: \n")
            user_info = get_user_info(username,cursor)
            break
    while True:
        try:
            print("*****************************************")
            print("In this Bank's App, you have 4 options\n"
                  "1. Deposit\n"
                  "2. Withdraw\n"
                  "3. Manage account\n"
                  "4. Exit")
            print("*****************************************\n")
            user_input = int(input("Choose 1-4: \n"))
            if user_input == 1:
                amount = float(input("Deposit amount(limit 9999.99!): \n"))
                deposit_amount(username= username, amount= amount,cursor= cursor,conn= conn)
                continue
            elif user_input == 2:
                amount = float(input("Withdraw amount(limit 9999.99!): \n"))
                withdraw_amount(username= username, amount= amount,cursor= cursor, conn= conn)
                continue
            elif user_input == 3:
                menu(username=username,cursor=cursor,conn=conn)
                continue
            elif user_input == 4:
                print("Exitting")
                break
        except ValueError:
            print("Input correct values!")
            continue
        except Exception as e:
            print("Something went wrong", e)
            break

if __name__ == "__main__":
    main()

