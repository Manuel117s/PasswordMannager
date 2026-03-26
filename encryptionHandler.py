import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64

def generate_key(password: str, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=480000
    )

    key = base64.urlsafe_b64decode(kdf.derive(password.encode()))
    return key

def encrypt_database(key ,salt):
    f = Fernet(key=key)
    encryptedDatabase = f.encrypt(b"passwords.db")

    