import random
import string

print("Welcome to Anushka's Password Generator! ❤️")

number = int(input("How many passwords do you want? "))
length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(number):
    password = ""

    for j in range(length):
        password += random.choice(characters)

    print("Password", i + 1, ":", password)

print("Thank you for using my Password Generator! ❤️")