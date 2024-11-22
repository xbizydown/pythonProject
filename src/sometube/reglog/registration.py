import sqlite3
import hashlib

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('../database/users.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                              (username TEXT PRIMARY KEY, age INTEGER, password TEXT)''')

    def add_user(self, username, age, password):
        try:
            self.cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (username, age, password))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Username already exists. Please choose a different username.")

    def get_all_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

class User:
    def __init__(self, username, password, password_confirm, age):
        self.username = username
        self.password = password
        self.password_confirm = password_confirm
        self.age = age

    def check_length(self):
        return 8 <= len(self.password) <= 32

    def check_spelling(self):
        return self.password == self.password_confirm

    def check_symbols(self):
        return self.password.isalnum()

def make_user():
    database = Database()
    user = User(input("Username: "), input("Password: "), input("Confirm password: "), int(input("Age: ")))

    if not user.check_length():
        exit("Your password should contain minimum of 8 characters, and maximum of 32 characters")

    if not user.check_spelling():
        exit("Your passwords don't match")

    if not user.check_symbols():
        exit("No special symbols allowed! Password format A-Z a-z 0-9")

    if user.age < 0:
        exit("Age can't be zero or negative")

    if user.age > 100:
        exit("Age can't be more than 100")

    if user.age % 1 != 0:
        exit("Age can't be a decimal number")

    hash_object = hashlib.sha256(user.password.encode('utf-8'))
    user.password = hash_object.hexdigest()

    database.add_user(user.username, user.age, user.password)

    print("Current users in the database:")
    for username, age, password in database.get_all_users():
        print(f"Username: {username}, Age: {age}, Password: {password}")

    database.close()

if __name__ == '__main__':
    make_user()