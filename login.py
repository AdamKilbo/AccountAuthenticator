import json

class login:
	def __init__(self):
		self.name = ""
		self.password = ""

	# thanks to stackoverflow user "smehmood" for this function
	def encode(self, string):
		encoded_chars = []
		key = "Hello, World!"
		for i in xrange(len(string)):
			key_c = key[i % len(key)]
			encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
			encoded_chars.append(encoded_c)
		encoded_string = "".join(encoded_chars)
		return base64.urlsafe_b64encode(encoded_string)

	def promptUsername(self):
		print "Please enter your account name: "
		self.name = raw_input()

	def promptpassword(self):
		print "Please enter your password: "
		self.password = raw_input()



	def main(self):
		self.promptUsername()
		self.promptPassword()

