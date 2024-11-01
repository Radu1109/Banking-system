import pymysql

def connect_to_database():
    '''Conectare la baza de date din MySql'''
    return pymysql.connect(
        host="localhost",
        user="root",
        password="radumihai01",
        database="mydb",
        port=3306
    )
def get_user_balance(username,cursor) -> float:
    """
    Returnează soldul curent al utilizatorului specificat.

    Argumente:
        username : Username-ul contului utilizatorului .
        cursor: Cursoul de acces la baza de date.

    Returneaza:
        float: Soldul utilizatorului.

    Note:
        Această funcție este definită în modulul `database.py`.
    """
    cursor.execute('''SELECT money FROM customers
    WHERE username = %s''',(username,))
    balance = float(cursor.fetchone()[0])
    return balance

def get_user_info(username,cursor) -> list:
    '''
    Informatiile utilizatorului din baza de date

    Argumente:

     username: Username-ul contului utilizatorului.
     cursor: Cursoul de acces la baza de date.
    :return: list.

    Note:
    Această funcție este definită în modulul `database.py`.
    '''
    cursor.execute('''SELECT * FROM customers
    WHERE username = %s''',(username,))
    account = cursor.fetchone() #Variabila account va stoca datele din b.d. sub forma de lista
    if account:
        ''' 
            Bucla infinita while True: este folosita pentru a continua
        folosirea programului chiar si dupa blocul
        try-except prinde vreo eroare umana sau a codului
        '''
        while True:
            try:
                pin_input = input("To access this account, you have to enter the PIN: \n").strip()
                if pin_input == account[5]:
                    return account
                else:
                    print("Wrong PIN")
                    continue
            except ValueError:
                print("Input correct values!")
                continue
            except Exception as e:
                print("Something went wrong", e)
    else:
        print("No account has been found")

