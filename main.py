import dataBaseHandler
import encryptionHandler
import os
from pathlib import Path

key = ""
salt = ""

def main():
    filePath = Path("passwords.db")

    if not filePath.exists:
        print("The setup of the app is going to start, follow the following instructions!")
        prepare_data_base()

def prepare_data_base():
    password = input("Enter a password: ")
    salt = os.urandom(16)
    key = encryptionHandler.generate_key(password=password, salt=salt)

    dataBaseHandler.create_database()
    


def close_program():
    dataBaseHandler.close_conection()

    
    

if __name__ is "__main__":
    main()