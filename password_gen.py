import random
import string


def generate_password(length=12):
    if length < 4:  # Ensure minimum length for a secure password
        raise ValueError("Password length must be at least 4 characters.")
            
# Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
   # symbols = string.punctuation
            
# Ensure password contains at least one of each type
    all_characters = lower + upper + digits #+ symbols
    password = [
    random.choice(lower),
    random.choice(upper),
    random.choice(digits),
   # random.choice(symbols)
            ]
            
# Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)
            
# Shuffle the password to avoid predictable patterns
    random.shuffle(password)
            
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Generated password:", generate_password(7))