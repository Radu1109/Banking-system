import pymysql

conn = pymysql.connect(
    host= "localhost",
    user= "root",
    password= "radumihai01",
    database= "mydb",
    port= 3306
)

cursor = conn.cursor()
class Account:
    def __init__(self) -> None:
        '''
        Construirea obiectului de tip Account

        Argumente: self

        return: None

        Note:
            Functia se gaseste in Account.py
        '''
        print("Input the following data\n")
        while True:
            try:
                self.first_name = input("Your first name = \n")
                if not self.first_name.isalpha(): #Utilizatorul este obligat sa introduca doar litere
                    print("Input only letters!")
                    continue
                self.last_name = input("Your last name = \n")
                if not self.last_name.isalpha(): #Utilizatorul este obligat sa introduca doar litere
                    print("Input only letters")
                    continue
                self.email = input("Your email address = \n") + "@" + input("Email type (yahoo, gmail, etc): ").lower() + ".com"
                self.username = input("Your account username will be = \n")
            except ValueError: #In cazul in care utilizatorul introduce valori gresite
                print("Input correct values!")
            except Exception as e:
                print("Something went wrong",e)
            break
        while True:
            try:
                pin = input("Your pin must be of 4 digits = \n")
                if pin.isdigit() and len(pin) == 4: #Utilizatorul este obligat sa introduca un PIN format din 4 cifre.
                    self.pin = pin
                    break
                else:
                    print("Your input is wrong! Too little/too many digits")
                    continue
            except ValueError:
                print("You must input a value formed of 4 digits!")
                continue
            except Exception as e:
                print("Something went wrong",e)
            break
        self.money = 0

    def display_account(self) -> None:
        '''
        Afisarea propietatilor obiectului Account

        Argumente: self

        return: None

        Note:
            Functia se gaseste in Account.py
        '''
        try:
            account = {"first_name" : self.first_name,
                       "last_name" : self.last_name,
                       "email" : self.email,
                       "username" : self.username,
                       "pin" : self.pin,
                       "money" : self.money}
            for key,value in account.items():
                print(f"{key} = {value}")
        except Exception as e:
            print("Something went wrong",e)

    def insert_account_into_db(self,account) -> None:
        '''
        Salvarea propietatilor obiectului Account in b.d.

        Argumente: self

        return: None

        Note:
            Functia se gaseste in Account.py
        '''
        try:
            cursor.execute("INSERT INTO customers (first_name, last_name, email, username, pin, money) VALUES (%s, %s, %s, %s, %s, %s)"
                           ,(account.first_name,account.last_name,account.email,account.username,account.pin,account.money))
            conn.commit()
        except Exception as e:
            print("Something went wrong",e)
            conn.rollback()

