import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password():
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Password length must be a positive integer.")
            else:
                password = generate_password(length)
                print("Generated Password:",password)
        except ValueError:
            print("Invalid input. Please enter a valid postive integer for password length.")       

password()
