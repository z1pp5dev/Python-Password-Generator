#Password Generator Project Week 3 Milestone

#Importing Random Library

import random

#Defining Character Pools

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_?+()"

#Main Generator Function

def generate_password ():
    #all_chars = letters + nums_symbols
    random_pass = ""
#Logic to select random characters/length
    for _ in range(10):
        random_pass += random.choice(characters)
    return random_pass


#Calling Pass Gen Function
new_pass = generate_password()

print(f"Your Password is: {new_pass}")
