
class User(object):
	"""implements users"""
	def __init__(self,username,password):
		self.users = []
		self.username = username
		self.password = password

	def save(self):
		user_id = str(len(self.users)+1)
		new_user = {
			"id": user_id,
			"username": self.username,
			"password": self.password
		}
		self.users.append(new_user)
		print("User signup successful")

	def get_users(self):
		return self.users

	def login(self):
		for user in self.users:
			if user["username"] == self.username:
				if user["password"] == self.password:
					print ("Login sucess!")
				print ('Incorrect password!')
			print("User doesn't exists!")



