
def user_transaction(username,amount,cursor,conn) -> None:
    """
    Saves the transaction in the database.

    Arguments:
        username: The username of the user's account.
        amount: The amount used in the transaction.
        cursor: The cursor to access the database.
        conn: The connection to the database.

    Returns:
        None.

    Note:
        This function is defined in the `transactions.py` module.
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