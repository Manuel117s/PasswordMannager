# Password Manager

A secure, command-line password manager that encrypts your passwords and stores them locally.

## Overview

This Password Manager is a Python-based application that allows you to securely store, manage, and retrieve passwords. All passwords are encrypted using industry-standard encryption (Fernet with PBKDF2-HMAC-SHA256) and protected by a master password of your choice.

## Features

✅ **Secure Encryption** - All passwords are encrypted using Fernet encryption with PBKDF2-HMAC-SHA256 key derivation (480,000 iterations) for maximum security

✅ **Master Password Protection** - Set up a master password on first use to encrypt/decrypt your entire database

✅ **Add Passwords** - Store new passwords with associated service names and usernames

✅ **Retrieve Passwords** - Look up passwords by service name

✅ **View All Passwords** - Display all stored passwords at once

✅ **Update Passwords** - Modify existing passwords in your database

✅ **Delete Passwords** - Remove passwords you no longer need

✅ **Local Storage** - All data is stored locally in an encrypted SQLite database (no cloud sync)

✅ **Auto-Encryption** - Passwords are automatically encrypted when you exit the program

## System Requirements

- Python 3.7 or higher
- Windows, macOS, or Linux

## Installation

1. Download the .exe from the "Release" section of this repository
2. Copy it to a folder where can be located
3. Run the application

## Usage

### First Time Setup

On first run, you'll be prompted to create a master password:
```
Enter a password: [your master password]
```

**⚠️ IMPORTANT:** Do not lose your master password! If you forget it, all your stored passwords will remain encrypted and inaccessible.

### Commands

Once logged in, use the following commands:

| Command | Description |
|---------|-------------|
| `list` | Show all available commands |
| `add` | Add a new password to the database |
| `get` | Retrieve a specific password by service name |
| `getall` | Retrieve and display all stored passwords |
| `update` | Update an existing password |
| `delete` | Delete a password from the database |
| `clear` | Clear the screen |
| `exit` | Exit the program and encrypt the database |

### Example Workflow

```
Enter a password: myMasterPassword123
SUCCESS
Welcome to the password manager, select an option or type "list" to show a list of all available options:

Enter an option: add
Enter the following data to add a new password to the database:
Service name: Gmail
User: myemail@gmail.com
Password: mySecurePassword
The password has been added successfully

Enter an option: get
Enter the name of the service to retrieve the password:
Service name: Gmail
Found password:
Service name | User | Password
('Gmail', 'myemail@gmail.com', 'mySecurePassword')

Enter an option: exit
The program is going to close, see you later!
```

## Security Features

- **Military-grade encryption** using Fernet (symmetric encryption)
- **Key derivation** using PBKDF2-HMAC-SHA256 with 480,000 iterations
- **Random salt** generation for each database
- **Local storage only** - no data is sent to external servers
- **Automatic encryption** on exit - database is encrypted when you close the program
- **Password-protected login** - master password required on each session

## File Structure

- `main.py` - Main application and user interface
- `dataBaseHandler.py` - SQLite database operations
- `encryptionHandler.py` - Encryption and decryption logic
- `passwords.db` - Your encrypted database (created on first run)

## License

This project is provided as-is for personal use.

## Disclaimer

This password manager stores passwords locally on your device. While encryption is used to protect your data, the security of your passwords ultimately depends on:
- The strength of your master password
- The security of your device
- Regular backups of your `passwords.db` file

Always keep your master password secure and never share it with anyone.
