import dataBaseHandler
import encryptionHandler
import os
from pathlib import Path

key = b""
salt = b""

def prepare_data_base():
    global key
    password = input("Enter a password: ")
    salt = os.urandom(16)
    key = encryptionHandler.generate_key(password=password, salt=salt)

    dataBaseHandler.create_database()
    print("The password has been added succesfully. DONT LOOSE THIS PASSWORD, OR ALL THE PASSWORD WILL REMAIN ENCRYPTED")

def close_program():
    dataBaseHandler.close_conection()
    encryptionHandler.encrypt_database(key=key, salt=salt)

def main():
    filePath = Path("passwords.db")

    if filePath.exists:
        print("The setup of the app is going to start, follow the following instructions!")
        prepare_data_base()
        close_program() #DEBUG

if __name__ == "__main__":
    main()