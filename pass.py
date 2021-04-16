import random


def createpassword(length):
	password = ""
	for i in range(length):
		password += chr(random.randrange(97, 122))
	print("Your password is:", password)


createpassword(8)
