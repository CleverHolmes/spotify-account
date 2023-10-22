import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # Generate from letters and digits
    print(characters)
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Generate a random string of length 6
random_string = generate_random_string(16)
print(random_string)