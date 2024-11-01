
def user_transaction(username,amount,cursor,conn) -> None:
    """
        Salveaza tranzactia in baza de date

        Argumente:
            username : Username-ul contului utilizatorului.
            amount: Suma folosita in tranzactie
            cursor: Cursoul de acces la baza de date.
            conn: Conexiunea la baza de date

            return: none

        Note:
            Această funcție este definită în modulul `transactions.py`.
        """
    cursor.execute('''SELECT id_customer FROM customers
    WHERE username = %s''',(username,))
    id_customer = cursor.fetchone()[0]
    try:
        cursor.execute('''INSERT INTO transactions(amount,id_customer) VALUES(%s,%s)''',(amount,id_customer))
        conn.commit()
        print("Transaction recorded successfully!")
    except Exception as e:
        print("Something went wrong!",e)
        conn.rollback()