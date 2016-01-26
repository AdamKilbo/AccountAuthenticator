# This program will make a user account

import json

# Class used in process of creating name and password for a user. Proposed name is stored in name. Proposed password is stored in password.
#  The name is checked against username rules and the database to make sure it does not exist. The password is checked for strength.
#  If these tests are passed, the Check variables will be changed to true and the system will create and store the user/pass combo. 
class createUser:
	def __init__(self):
		self.name = ""
		self.password = ""
		self.usernameCheck = False
		self.passwordCheck = False

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
		self.usernameCheck = True
		# WIP, doesn't actually check anything. Should parse for characters.

	# checks password strength. If password is appropriately strong, returns 0. 
	# Else returns negative number. Currently only checks length.
	def checkPasswordRules(self):
		if self.password and len(self.password) > 5:
			self.passwordCheck = True
		# WIP, add additional strength checks

	def createUserAccount(self):
		print ("Hello, user! Thanks for creating an account!")

		# Prompt for username and password for new account
		self.promptUsername()
		self.promptPassword()

		# Ensure that username and password are legal
		# If passed, self.usernameCheck and self.passwordCheck are TRUE
		self.checkUserRules()
		self.checkPasswordRules()

		# if checksum's are passed, store username/pass combo
		if self.usernameCheck == True and self.passwordCheck == True:

			data = {}
			data['name'] = self.name
			data['password'] = self.password
			print json.dumps(data, indent = 2, sort_keys=False)
			with open('accounts.txt', 'a') as outfile:
				json.dump(data, outfile)

		if self.passwordCheck == False:
			print("Bad password")

		if self.usernameCheck == False:
			print("Bad username")

		# Returns. If success, return 0. Else, return negative number.
		return 0

def main():
	CREATEUSER = createUser()
	CREATEUSER.createUserAccount()

	return 0

main()

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
"""