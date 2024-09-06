import random
import string

def generate_password(length):
    # Define the character to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

        # Randomly choose characters from the defined set
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Ask the user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate the password and display it
password = generate_password(password_length) 
print("Generated password:", password)

