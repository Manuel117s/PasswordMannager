import sqlite3

def create_database():
    execute_query("CREATE TABLE IF NOT EXISTS passwords(serviceName, user, password)")

def insert_data(serviceName: str, user: str, password: str):
    query = "INSERT INTO passwords(serviceName, user, password) VALUES (?, ?, ?)"
    execute_query(query, parameters=(serviceName, user, password))
        
def retrive_password(serviceName: str):
    query = "SELECT * FROM passwords WHERE serviceName = ?"
    row = execute_query(query, parameters=(serviceName,), returnData=True)

    if row:
        print("Found password:")
        print("Service name | User | Password")
        print(row)
    else:
        print("No data on the row")

def retrive_all_passwords():
    query = "SELECT * FROM passwords"
    rows = execute_query(query, returnAll=True)
    if rows:
        print("All passwords on the database:")
        print("Service name | User | Password")
        for row in rows:
            print(row)
    else:
        print("No data on the database")

def update_password(serviceName: str, newPassword: str):
    query = "UPDATE passwords SET password = ? WHERE serviceName = ?"
    execute_query(query, parameters=(newPassword, serviceName))

def delete_password(serviceName: str):
    query = "DELETE FROM passwords WHERE serviceName = ?"
    execute_query(query, parameters=(serviceName,))

def execute_query(query: str, parameters: tuple = (), returnData: bool = False, returnAll: bool = False):
    """
    Execute a SQL query and return the result based on the specified parameters. IMPORTANT: Is important to set one of the return parameters to True, if both are False, the function will return None, and if both are True, the function will return all the data from the query.

    Args:
        query (str): The SQL query to be executed.
        parameters (tuple, optional): The parameters to be passed to the SQL query. Defaults to an empty tuple.
        returnData (bool, optional): If True, returns a single row of data. Defaults to False.
        returnAll (bool, optional): If True, returns all rows of data. Defaults to False.
    Returns:
        The result of the SQL query based on the specified parameters.
    """
    with sqlite3.connect("passwords.db") as conection:
        cursor = conection.cursor()
        cursor.execute(query, parameters)

        if returnData:
            return cursor.fetchone()
        elif returnAll:
            return cursor.fetchall()
        
        conection.commit()