import random
import string
# command line
import sys

def generate_password(length):
      # Define characters we want to use
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ""
    
    for i in range(length):
        random_char = random.choice(characters)
        password+=(random_char)

    return password
    

print("--- Welcome to the Simple Password Generator ---")


if len(sys.argv) < 2:

  user_length = int(input("How many characters should the password be? "))
else:
  user_length = int(sys.argv[1])


new_password = generate_password(user_length)
print(f"Your new password is: {new_password}")