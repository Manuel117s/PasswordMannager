import sqlite3
conection = sqlite3.connect("tutorial.db")

def create_database():
    execute_query("CREATE TABLE IF NOT EXISTS passwords(serviceName, user, password)", False)

def insert_data(serviceName: str, user: str, password: str):
    execute_query(f"""
        INSERT INTO passwords(serviceName, user, password)
        VALUES ({serviceName}, {user}, {password})
                    """, False)
        
def retrive_password(serviceName: str):
    row = execute_query(f"SELECT * FROM services WHERE serviceName = '{serviceName}'", True)

    if row:
        print(row)
    else:
        print("No data on the row")

def execute_query(query: str, returnData: bool):
    with conection:
        cursor = conection.cursor()
        cursor.execute(query)

        if returnData:
            row = cursor.fetchone
            return row

def close_conection():
    conection.close()