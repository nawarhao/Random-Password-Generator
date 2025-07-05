import random
import string

def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    # Combine all characters
    all_chars = lower + upper + digits

    # Generate password with a mix of characters
    password = random.sample(all_chars, length)

    # Shuffle the password
    random.shuffle(password)

   
    return ''.join(password)


print("Generated Password:", generate_password())
