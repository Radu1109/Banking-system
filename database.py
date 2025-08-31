import pymysql

def connect_to_database():
    '''Connecting to MySql data base'''
    conn = pymysql.connect(
        host="localhost",
        user="YOUR USERNAME",
        password="YOURPASSWORD",
        database="mydb",
        port=3306
    )
    return conn
def get_user_balance(username,cursor) -> float:
    """
    Arguments:
    username: The username of the user's account.
    cursor: The cursor to access the database.

    Returns:
    float: The user's balance.

    Notes:
    This function is defined in the `database.py` module.
    """
    cursor.execute('''SELECT money FROM customers
    WHERE username = %s''',(username,))
    balance = float(cursor.fetchone()[0])
    return balance

def get_user_info(username,cursor) -> list:
    '''
    Getting user's info

    Arguments:

    username: The username of the user's account.
    cursor: The cursor to access the database.
    :return: list.

    Notes:
    This function is defined in the `database.py` module.
    '''
    cursor.execute('''SELECT * FROM customers
    WHERE username = %s''',(username,))
    account = cursor.fetchone() #Variabila account va stoca datele din b.d. sub forma de lista
    if account:
        ''' 
            The infinite while True loop is used to keep the program running 
        even after the try-except block catches a human or code error.
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

