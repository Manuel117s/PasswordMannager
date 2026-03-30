import dataBaseHandler
import encryptionHandler
import os
import sys
from pathlib import Path

key = b""
salt = b""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def prepare_data_base():
    global key
    global salt

    password = input("Enter a password: ")
    salt = os.urandom(16)
    key = encryptionHandler.generate_key(password=password, salt=salt)

    dataBaseHandler.create_database()
    print("The password has been added succesfully. DONT LOOSE THIS PASSWORD, OR ALL THE PASSWORD WILL REMAIN ENCRYPTED")

def login():
    global key
    global salt

    password = input("Enter the password (Or type _exit to close the program): ")
    if password == "_exit":
        return

    success, message, returnedKey, returnedSalt = encryptionHandler.decrypt_database(password=password)

    if success:
        key = returnedKey
        salt = returnedSalt 
        print("SUCCESS")
    else:
        print("Error, try again")
        login()

def close_program():
    if key != b"":
        encryptionHandler.encrypt_database(key=key, salt=salt)
        print("The program is going to close, see you later!")
        sys.exit()

def add():
    print("Enter the following data to add a new password to the database:")
    serviceName = input("Service name: ")
    user = input("User: ")
    password = input("Password: ")
    dataBaseHandler.insert_data(serviceName=serviceName, user=user, password=password)
    print("The password has been added succesfully")

def get():
    print("Enter the name of the service to retrieve the password:")
    serviceName = input("Service name: ")
    dataBaseHandler.retrive_password(serviceName=serviceName)

def get_all():
    print("Retrieving all passwords...")
    dataBaseHandler.retrive_all_passwords()

def update():
    print("Enter the name of the service to update the password:")
    serviceName = input("Service name: ")
    newPassword = input("New password: ")
    dataBaseHandler.update_password(serviceName=serviceName, newPassword=newPassword)

def delete():
    print("Enter the name of the service to delete the password:")
    serviceName = input("Service name: ")
    dataBaseHandler.delete_password(serviceName=serviceName)

def main_screen():
    print("Welcome to the password manager, select an option or type \"list\" to show a list of all available options:")  
    option = input("Enter an option: ").lower()

    match option:
        case "list":
            print("" \
            "list - Show a list of all avalible options\n" \
            "add - Add a new password to the database\n" \
            "get - Get a password from the database, requires the name of the service\n"\
            "getall - Get all the passwords from the database\n"\
            "update - Update a password from the database, requires the name of the service\n"\
            "delete - Delete a password from the database, requires the name of the service\n"\
            "exit - Exit the program and encrypt the database\n"
            )
        case "add":
            add()
        case "get":
            get()
        case "getall":
            get_all()
        case "update":
            update()
        case "delete":
            delete()
        case "exit":
            close_program()
        case "clear":
            clear_screen()
        case _:
            print("Invalid option, try again")

    main_screen()

def main():
    filePath = Path("passwords.db")

    if not filePath.exists():
        print("The setup of the app is going to start, follow the following instructions!")
        prepare_data_base()
        close_program()
    
    login()
    main_screen()

if __name__ == "__main__":
    main()