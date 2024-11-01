import database
from database import get_user_balance
from transactions import user_transaction
def deposit_amount(username,amount,cursor,conn):

    '''
    Deposit money into user's account

    Arguments:
    - username: The username of the user's account.
    - amount: The amount entered by the user.
    - cursor: The cursor to access the database.
    - conn: Represents the active connection to the database.
    - return: None.

    Note:
    Function defined in account_management.py.
    '''

    money = get_user_balance(username, cursor)
    limit = 9999.99

    ''' 
        The infinite while True loop is used to keep the program running 
    even after the try-except block catches a human or code error.
    '''
    while True:
        try:

            if amount > limit:
                print(f"You cannot deposit more that {limit}!")
                continue
            elif amount <= 0:
                print("You cannot deposit 0 money nor a negative sum!")
                continue
            elif amount + money > limit:
                cursor.execute('''
                            UPDATE customers
                            SET money = %s
                            WHERE username = %s
                            ''', (limit,username))
                conn.commit()
                rest_i = limit - money
                rest_f = amount - rest_i

                '''
                    If the amount entered by the user exceeds the program limit,
                the program will store the excess in the variable "rest_i(initial)"
                and subtract it from the entered amount to find the remainder,
                stored in the variable "rest_f(final)".
                '''
                user_transaction(username= username, amount= amount, cursor= cursor, conn= conn)

                print(f"Deposit was successful, but the amount exceeded our {limit}, return {rest_f}")
                break #The program exits the infinite loop because it has achieved its purpose.
            else:
                cursor.execute('''
                            UPDATE customers
                            SET money = money + %s
                            WHERE username = %s
                            ''', (amount, username))
                conn.commit()

                user_transaction(username=username, amount=amount, cursor=cursor, conn=conn)

                print("Deposit successful!")
                break
        except ValueError: #This except block catches any ValueError caused by the user, e.g., entering a string for the amount variable.
            print("You must input correct values!")
        except Exception as e: #This except block catches any other errors by the program.
            print("Something went wrong", e)


def withdraw_amount(username,amount,cursor,conn):

    '''
    Withdraw money from the user's account.

    Arguments:

        username: The username of the user's account.
        amount: The amount entered by the user.
        cursor: The cursor to access the database.
        conn: Represents the active connection to the database.
        return: None.

    Note:

        Function defined in `account_management.py`.
    '''

    money = money = get_user_balance(username,cursor) #
    limit = 9999.99

    ''' 
        The infinite while True loop is used to keep the program running 
    even after the try-except block catches a human or code error.
    '''
    while True:
        try:
            if amount > limit:
                print("You cannot withdraw that much money!")
                continue
            elif amount <= 0:
                print("You cannot withdraw 0 money nor a negative sum!")
                continue
            elif amount > money:
                print("Insufficent funds")
                continue
            elif amount == money:
                print("Withdraw successful, balance is empty")
                user_transaction(username=username, amount=amount, cursor=cursor, conn=conn)
                break
            else:
                '''
                    If all conditions are met, the database will be updated 
                to save the change of withdrawing x amount of money 
                from the user's account.
                '''
                cursor.execute('''
                    UPDATE customers
                    SET money = money - %s
                    WHERE username = %s
                    ''', (amount, username))
                conn.commit()
                user_transaction(username=username, amount=amount, cursor=cursor, conn=conn)
                break
        except ValueError:
            print("You must input correct values!")
        except Exception as e:
            print("Something went wrong", e)
            print("Withdraw successful!")

def menu(username,cursor,conn):
    '''
    User account menu.

    Arguments:

    :param username: The username of the user's account.
    :param cursor: The cursor to access the database.
    :param conn: Represents the active connection to the database.
    :return: None.

    Note:
        Function defined in `account_management.py`.
    '''
    while True:
        try:
            print("You have the next options: \n"
                  "1. Change lastname\n"
                  "2. Change email\n"
                  "3. Change username\n"
                  "4. Change PIN\n"
                  "5. Exit")
            manage_input = int(input("Choose what you want to do: \n"))
            if manage_input == 1:
                lastname_input = input("What will be your new lastname?")
                if lastname_input.isalpha():
                    cursor.execute('''
                                    UPDATE customers
                                    SET last_name = %s
                                    WHERE username = %s
                                    ''', (username, lastname_input))
                    conn.commit()
                    print(f"Last name changed successfully in {lastname_input}")
                    break
                else:
                    print("Your name should not contain numbers!")
                    continue
            elif manage_input == 2:
                email_input = input("What will be your new email?\n"
                                    "PLEASE write whole email! ex: abcd@yahoo.com")
                cursor.execute('''
                                    UPDATE customers
                                    SET email = %s
                                    WHERE username = %s
                                    ''', (username, email_input))
                conn.commit()
                print(f"Email changed successfully in {email_input}")
                break
            elif manage_input == 3:
                username_input = input("What will be your new username?")
                cursor.execute('''
                                    UPDATE customers
                                    SET username = %s
                                    WHERE username = %s
                                    ''', (username, username_input))
                conn.commit()
                print(f"Username changed successfully in {username_input}")
                break
            elif manage_input == 4:
                pin_input = input("What will be your new PIN?")
                if pin_input.isdigit() and len(pin_input) == 4:
                    cursor.execute('''
                                        UPDATE customers
                                        SET `pin` = %s
                                        WHERE username = %s
                                        ''', (username, pin_input))
                    conn.commit()
                    print(f"PIN changed successfully in {pin_input}")
                    break
                else:
                    print("Your pin must be of 4 digits!")
                    continue
            elif manage_input == 5:
                print("Exit")
                break
            else:
                print("Input a number 1-5!")
                continue
        except ValueError:
            print("Input correct values!")
        except Exception as e:
            print("Something went wrong", e)