import random
import string

# Function to generate a new API key
def generate_api_key():
    api_key = ''.join(random.choices(string.ascii_letters + string.digits, k=54))
    return api_key

for i in range(50):
    print(generate_api_key())
