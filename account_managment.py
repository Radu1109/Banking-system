import database
from database import get_user_balance
from transactions import user_transaction
def deposit_amount(username,amount,cursor,conn):

    '''
    Functia de depozitare a banilor in contul userului

    Argumente:
        username: Username-ul contului utilizatorului
        amount: Suma introdusa de utilizator,
        cursor: Cursoul de acces la baza de date,
        conn: Reprezinta conexiunea activa la b.d.
        return = None

    Nota:

        Functie definita in `account_managment.py`
    '''

    money = get_user_balance(username, cursor)
    limit = 9999.99

    ''' 
        Bucla infinita while True: este folosita pentru a continua
    folosirea programului chiar si dupa blocul
    try-except prinde vreo eroare umana sau a codului
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
                    Daca suma introdusa de utilizator este mai mare decat limita impusa de program,
                programul va stocla suma care este necesara pentru atingerea limitei programului prin variabila
                "rest_i(initial)" si o va scadea din suma introdusa de utilizator, pentru a afla restul, stocat
                in variabila rest_f(final)
                '''
                user_transaction(username= username, amount= amount, cursor= cursor, conn= conn)

                print(f"Deposit was successful, but the amount exceeded our {limit}, return {rest_f}")
                break #Programul inceteaza bucla infinita pentru ca si-a atins scopul.
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
        except ValueError: #Acest except prinde orice ValueError cauzat de user, ex: introducerea unui string pentru variabila amount
            print("You must input correct values!")
        except Exception as e: #Acest except va prinde oricare alta eroare cauzata de program
            print("Something went wrong", e)


def withdraw_amount(username,amount,cursor,conn):

    '''
    Functia de extragere a banilor din contul userului

    Argumente:

        username: Username-ul contului utilizatorului
        amount: Suma introdusa de utilizator,
        cursor: Cursoul de acces la baza de date,
        conn: Reprezinta conexiunea activa la b.d.
        return = None

    Nota:

        Functie definita in `account_managment.py`
    '''

    money = money = get_user_balance(username,cursor) #
    limit = 9999.99

    '''
        Bucla infinita while True: este folosita pentru a continua
    folosirea programului chiar si dupa blocul
    try-except prinde vreo eroare umana sau a codului
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
                    Daca toate conditiile au fost indeplinite, baza de date va fi updatata
                astfel incat sa fie salvata modificarea de retragerea a x sume de bani
                din contul utilizatorului
                '''
                cursor.execute('''
                    UPDATE customers
                    SET money = money - %s
                    WHERE username = %s
                    ''', (amount, username))
                conn.commit()
                user_transaction(username=username, amount=amount, cursor=cursor, conn=conn)
                break #Programul inceteaza bucla infinita pentru ca si-a atins scopul.
        except ValueError: #Acest except prinde orice ValueError cauzat de user, ex: introducerea unui string pentru variabila amount
            print("You must input correct values!")
        except Exception as e: #Acest except va prinde oricare alta eroare cauzata de program
            print("Something went wrong", e)
            print("Withdraw successful!")

def menu(username,cursor,conn):
    '''
    Meniul contului utilizatorului

    Argumente:

    :param username: Username-ul contului utilizatorului
    :param cursor: Cursoul de acces la baza de date
    :param conn: Reprezinta conexiunea activa la b.d.
    :return: None

    Note:
        Functie definita in `account_managment.py`
    '''

    '''
        Bucla infinita while True: este folosita pentru a continua
    folosirea programului chiar si dupa blocul
    try-except prinde vreo eroare umana sau a codului
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