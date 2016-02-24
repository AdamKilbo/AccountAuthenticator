import accountmaker
import login

def main():
	print("Hello user! What would you like to do? \n 1. Login \n 2. Register Account")
	userInput = raw_input()

	if userInput == "1":
		LOGIN = login.login()
		LOGIN.main()

	elif userInput == "2":
		CREATEUSER = accountmaker.createUser()
		CREATEUSER.createUserAccount()

	else:
		print("Number not recognized, please try again")

	return 0

if __name__ == "__main__":
	main()