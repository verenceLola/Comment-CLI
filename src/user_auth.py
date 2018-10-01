from users import User
import getpass

username = input("Enter Your username..")
password = getpass.getpass("Enter Your password..")


def create_user():
	userdata = User(username,password)
	userdata.save()



def login_user():
	userdata = User(username,password)
	userdata.login()

create_user()
login_user()