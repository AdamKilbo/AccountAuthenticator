# This program will make a user account


# Class used in process of creating name and password for a user. Proposed name is stored in name. Proposed password is stored in password.
#  The name is checked against username rules and the database to make sure it does not exist. The password is checked for strength.
#  If these tests are passed, the Check variables will be changed to true and the system will create and store the user/pass combo. 
class createUser:
	def __init__(self):
		self.name = ""
		self.password = ""
		self.usernameCheck = False
		self.passwordCheck = False

	def updateName(name):
		self.name = name
		return 0

	def updatePassword(password):
		self.password = password
		return 0

	# prompts user for a username
	def promptUsername():
		print ("input your username: ")
		name = raw_input()
		self.updateName(name)
		print ("your username is", self.name)
		return 0

	def promptPassword():
		print ("input your password: ")
		password = raw_input()
		self.updatePassword(password)
		print ("your password is", self.password)
		return 0

	# checks to ensure that user can exist (doesn't violate naming rules, username doesn't exist in database).
	#def checkUserRules():
	#	return 0
		# WIP

	# checks password strength. If password is appropriately strong, returns 0. Else returns negative number.
	# currently only checks length
	#def checkPasswordRules():
	#	if self.password and len(self.password) < 5
	#		return -1
	#	return 0
		# WIP

	def createUserAccount():
		print ("Hello, user! Thanks for creating an account!")

		self.promptName(self)
		self.promptPassword(self)

		#self.checkUserRules(self)
		#self.checkPasswordRules(self)

		# if checksum's are passed, store username/pass combo
		print ("your username is ", self.name, " and your password is ", self.password)

		# Returns. If success, return 0. Else, return negative number.
		return 0

def main():
	print ("test 0")
	CREATEUSER = createUser()
	print ("test1")
	CREATEUSER.createUserAccount()
	print ("test 2")
	return 0;

"""
Future improvements:
	(initially)
	- Store in a key value pair (JSON)
	(when I prove that I can do the above)
	- Store passwords in a hash
	- Store usernames in a file that is not plaintext
	- Check to see if username already exists
	- Check password security (use numbers, capitals, symbols, etc.)

"""