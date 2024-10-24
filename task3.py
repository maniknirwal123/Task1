
import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = 'Manik@1234'.join(random.choice(characters) for _ in range(length))
    return password

password_length = 5  

generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")
