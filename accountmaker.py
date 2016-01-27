# This program will make a user account

import json

# This class used in process of creating name and password for a user. 
# Proposed name is stored in name. Proposed password is stored in password.
# The name is checked against username rules and the database to make sure it 
# does not exist. The password is checked for strength. If these tests are 
# passed, the Check variables will be changed to true and the system will 
# create and store the user/pass combo. 
class createUser:
	def __init__(self):
		self.name = "" # Proposed account username
		self.password = "" # Proposed account password
		self.usernameCheck = False # If legal username, this will be true
		self.passwordCheck = False # If legal password, this will be true

	def updateName(self, name):
		self.name = name
		return 0

	def updatePassword(self, password):
		self.password = password
		return 0

	# prompts user for a username
	def promptUsername(self):
		print ("input your username: ")
		name = raw_input()
		self.updateName(name)
		print ("your username is", self.name)
		return 0

	def promptPassword(self):
		print ("input your password: ")
		password = raw_input()
		self.updatePassword(password)
		print ("your password is", self.password)
		return 0

	# checks to ensure that user can exist (doesn't violate naming rules, username doesn't exist in database).
	def checkUserRules(self):
		if self.name and len(self.name) > 5:
			self.usernameCheck = True
		# WIP, only checks for username length

	# checks password strength. If password is appropriately strong, returns 0. 
	# Else returns negative number. Currently only checks length.
	def checkPasswordRules(self):
		if self.password and len(self.password) > 5:
			self.passwordCheck = True
		# WIP, add additional strength checks

	def registerUser(self):
		# The variable data is the JSON object constructed to hold the name and password of user account
		data = {}
		data['name'] = self.name
		data['password'] = self.password

		# Debugging, print the JSON object we constructed
		print json.dumps(data, indent = 2, sort_keys=False)

		# append JSON object to text file "accounts.txt"
		with open('accounts.txt', 'a') as outfile:
			json.dump(data, outfile)

	# If bad username was inputted by user, this is used to prompt for good one.
	def promptUsernameBad(self):
		while self.usernameCheck == False:
			print("Bad username, please try again")
			self.promptUsername()
			self.checkUserRules()

	# If bad password was inputted by user, this is used to prompt for good one.
	def promptPasswordBad(self):
		while self.passwordCheck == False:
			print("Bad password, please try again")
			self.promptPassword()
			self.checkPasswordRules()

	# This function controls the process of making a new account.
	def createUserAccount(self):
		print ("Hello, user! Thanks for creating an account!")

		# Prompt for username for new account
		self.promptUsername()
		# Ensure that username is legal
		self.checkUserRules()
		# If not legal, prompt until legal username is inputted
		if self.usernameCheck == False:
			promptUsernameBad()


		# Prompt for password for new account
		self.promptPassword()
		# Ensure that password is legal
		self.checkPasswordRules()
		# If not legal, prompt until legal password is inputted
		if self.passwordCheck == False:
			promptPasswordBad()


		# Register the user/pass combo as a JSON element in a text file.
		# Yes I know it is not secure, but that will come later.
		registerUser()

		return 0

"""
Future improvements:
	(initially)
	- Store as a JSON key value pair. (Finished)

	(when I prove that I can do the above)
	- Store passwords in a hash
	- Store usernames in a file that is not plaintext
	- Check to see if username already exists
	- Check password security (use numbers, capitals, symbols, etc.)

"""

""" 
Things I learned:

	- Python implicitly passes self object to class methods.
	- general using OOP to have specific functions
"""