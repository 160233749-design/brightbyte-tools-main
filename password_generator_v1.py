import random
import string

def generate_password(length):
      # Define characters we want to use
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = []
    
    for i in range(length):
        random_char = random.choice(characters)
        password.append(random_char)
    

print("--- Welcome to the Simple Password Generator ---")

user_length = int(input("How many characters should the password be? "))

new_password = generate_password(user_length)
print(f"Your new password is: {new_password}")