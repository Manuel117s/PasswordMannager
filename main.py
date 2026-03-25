import dataBaseHandler

def main():
    dataBaseHandler.create_database()
    dataBaseHandler.insert_data("Somebrowser", "Jhon Doe", "1234")
    dataBaseHandler.retrive_password("Somebrowser")

def close_program():
    dataBaseHandler.close_conection()
    

if __name__ is "__main__":
    main()