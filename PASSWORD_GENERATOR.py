import random
import string

def generate_password(length):
    if length < 4:  # Ensure the length is enough to include all character types
        print("Password length should be at least 4")
        return None

    # Define character sets
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_chars, k=length-4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        password = generate_password(length)
        if password:
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

