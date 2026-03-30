import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64

def createKdf(salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000
    )
    return kdf

def generate_key(password: str, salt):
    kdf = createKdf(salt=salt)

    key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
    return key

def encrypt_database(key ,salt):
    f = Fernet(key)
    with open("passwords.db", "rb") as file:
        dataBaseData = file.read()
    encryptedDatabase = f.encrypt(dataBaseData)

    with open("passwords.db", "wb") as file:
        file.write(salt + encryptedDatabase)

def decrypt_database(password: str):
    with open("passwords.db", "rb") as file:
        salt = file.read(16)
        encryptedData = file.read()
    
    kdf = createKdf(salt=salt)
    key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))

    f = Fernet(key=key)
    try:
        unecrypted_database = f.decrypt(encryptedData)
        #unecrypted_database.decode()

        with open("passwords.db", "wb") as file:
            file.write(unecrypted_database)
        return True, "Decryption succesfull, you can now access the database", key, salt
    except UnicodeDecodeError as e:
        return f"An error has ocurred: {e}"
    except Exception as e:
        return False, "You have entered a wrong password, or the database is corrupted. Try again.", None, None