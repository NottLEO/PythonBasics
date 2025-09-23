import random
import string
input("Would you like to generate a random password? (Press Enter to continue)")
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Random password:", generate_password(12))
