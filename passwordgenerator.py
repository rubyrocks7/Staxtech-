import random
import string

def generate_password(length=12):
    # Define the character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the generated password has the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example: Generate a password of length 12
password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)

print(f"Generated Password: {password}")
