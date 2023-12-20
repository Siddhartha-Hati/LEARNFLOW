import mysql.connector
from cryptography.fernet import Fernet
import json
import secrets
import string
import os
import hashlib


class PasswordManager:
    def __init__(self):
        self.key = self.generate_key()
        self.connection = self.connect_to_database()

    def generate_key(self):
        key_file = "key.key"
        if not os.path.exists(key_file):
            key = Fernet.generate_key()
            with open(key_file, "wb") as file:
                file.write(key)
        with open(key_file, "rb") as file:
            return file.read()

    def connect_to_database(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Babula@143",
            database="Password_vault"
        )

    def encrypt(self, data):
        cipher = Fernet(self.key)
        return cipher.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        cipher = Fernet(self.key)
        decrypted_data = cipher.decrypt(encrypted_data).decode()
        return decrypted_data

    def create_category_table(self, category):
        cursor = self.connection.cursor()
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {category} (website VARCHAR(255), username TEXT, password VARCHAR(200))")
        self.connection.commit()
        cursor.close()

    def save_password(self, category, website, username, password):
        cursor = self.connection.cursor()

        
        self.create_category_table(category)

        encrypted_password = self.encrypt(password)

        insert_query = f"INSERT INTO {category} (website, username, password) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (website, username, encrypted_password))

        self.connection.commit()
        cursor.close()

    def retrieve_password(self, category, website, username):
        cursor = self.connection.cursor(dictionary=True)
        select_query = f"SELECT username, password FROM {category} WHERE website = %s AND username= %s"
        cursor.execute(select_query, (website, username,))
        stored_data = cursor.fetchone()
        cursor.close()

        if stored_data:
            return {
                "password": self.decrypt(stored_data["password"])
            }
        else:
            return None

    def generate_password(self, length=12):
        punc = '!@#$^_+=-'
        characters = string.ascii_letters + string.digits + punc

       
        passwords = (
            secrets.choice(string.ascii_uppercase) +
            secrets.choice(string.digits) +
            secrets.choice(punc))

        
        passwords += ''.join(secrets.choice(characters) for _ in range(length - len(passwords)))

        
        password_list = list(passwords)
        secrets.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        return password


class Password_Manager(PasswordManager):
    def __init__(self):
        super().__init__()  
        self.hashed_master_password = self.hash_password("Babula@143")

    def hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def check_master_password(self, input_password):
        hashed_input_password = self.hash_password(input_password)
        return hashed_input_password == self.hashed_master_password



if __name__ == "__main__":
    password_manager = Password_Manager()
    input_password = input("Enter your master password: ")
    if password_manager.check_master_password(input_password):
        print("Master password is correct. Access granted.")
        while True:
            print("\n1. Generate password and Save")
            print("2. Save Password")
            print("3. Retrieve Password")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                category = input("Enter category: ")
                website = input("Enter website: ")
                username = input("Enter Username: ")
                password = password_manager.generate_password()
                password_manager.save_password(category, website, username, password)

            elif choice == "2":
                category = input("Enter category: ")
                website = input("Enter website: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                password_manager.save_password(category, website, username, password)
                print("Password saved successfully!")

            elif choice == "3":
                category = input("Enter category: ")
                website = input("Enter website: ")
                username = input("Enter username: ")
                stored_password = password_manager.retrieve_password(category, website, username)
                if stored_password:
                    print("\nPassword: {}".format(stored_password["password"]))
                else:
                    print("Password not found.")

            elif choice == "4":
                break

            else:
                print("Invalid choice. Please enter between 1-4.")
    else:
        print("Master password is incorrect. Access denied.")
