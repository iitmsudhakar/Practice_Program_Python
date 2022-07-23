class Profile:
    def __init__(self, username, password):
        self.username = username
        if self.check_password(password):
            self.password = password
            self.old_passwords = [password]
        else:
            self.password = None
            self.old_passwords = []

    def check_password(self, password):
        if len(password) > 7:
            # first = password[0]
            if password[0].isupper():
                for x in password:
                    if x.isalnum():
                        return True
            else:
                return False
        else:
            return False

    def change_password(self, password):
        if self.check_password(password) and password not in self.old_passwords:
            self.password = password
            self.old_passwords.append(password)

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("WELCOME")
        else:
            print("INVALID")
