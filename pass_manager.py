import sqlite3
from cryptography.fernet import Fernet
import os

def init_db():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

if os.path.exists('secret.key'):
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()

else:
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

cipher_suite = Fernet(key)

def encrypt_password(password):
    return cipher_suite.encrypt(password.encode())

def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password).decode()

def add_password(service, username, password):
    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO passwords (service, username, password)
        VALUES (?, ?, ?)
    ''', (service, username, encrypted_password))
    conn.commit()
    conn.close()
    print("Password saved successfully!")

def get_password(service):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, password FROM passwords WHERE service = ?
    ''', (service,))
    result = cursor.fetchone()
    conn.close()

    if result:
        username, encrypted_password = result
        decrypted_password = decrypt_password(encrypted_password)
        print(f"Service: {service}")
        print(f"Username: {username}")
        print(f"Password: {decrypted_password}")
    else:
        print("No password found for this service.")

def main():
    while True:
        print("\nPassword Manager")
        print("1. Add a password")
        print("2. Retrieve a password")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice =='1':
            service = input("Enter service (e.g., Gmail): ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(service, username, password)
        
        elif choice == '2':
            service = input("Enter service to retrieve: ")
            get_password(service)

        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()