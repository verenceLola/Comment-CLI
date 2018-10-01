import getpass

class User(object):
    """implements users"""
    def __init__(self):
        self.users = []


    def save(self):
        username = input("Enter Your username..")
        password = getpass.getpass("Enter Your password..")

        user_id = len(self.users)+1
        new_user = {
            "id": user_id,
            "username": username,
            "password": password
        }
        self.users.append(new_user)
        print("User signup successful")

    def get_users(self):
        return self.users

    def login(self):
        username = input("Enter Your username..")
        password = getpass.getpass("Enter Your password..")
        for user in self.users:
            if user["username"] == username:
                if user["password"] == password:
                    print ("Login sucess!")
                else:
                    print ('Incorrect password!')
            else:
                print("User doesn't exists!")