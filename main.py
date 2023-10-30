3. **Password Generator - Python**:

```python
import random
import string

def generate_password(length, include_uppercase, include_digits, include_special_chars):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if len(characters) == 0:
        return "Error: No character set selected"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
include_uppercase = input("Include uppercase letters (yes/no): ").lower() == "yes"
include_digits = input("Include digits (yes/no): ").lower() == "yes"
include_special_chars = input("Include special characters (yes/no): ").lower() == "yes"

password = generate_password(length, include_uppercase, include_digits, include_special_chars)
print("Generated Password: " + password)
