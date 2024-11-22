from src.sometube.reglog.registration import Database, User

class Authentication:
    def __init__(self, database=None):
        self.database = database if database else Database()

    def login(self, username, password, age):
        try:
            user = User(username, password, password, age)
            user.check_length()
            user.check_symbols()
            for registered_user in self.database.get_all_users():
                if user.username == registered_user[0] and user.password == registered_user[2] and user.age == registered_user[1]:
                    return True
        except (ValueError, TypeError):
            pass
        return False

    def get_all_users(self):
        return self.database.get_all_users()

    def close(self):
        self.database.close()

if __name__ == '__main__':
    username = input("Username: ")
    password = input("Password: ")
    age = None

    try:
        auth = Authentication()
        if auth.login(username, password, age):
            print(f"Login successful! Welcome {username}!")
        else:
            print("Login failed. Invalid username or password.")
    finally:
        auth.close()