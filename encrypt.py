import os
import random
import datetime

# Function to compute the password value
def compute_password_value(password):
    ascii_sum = sum(ord(char) for char in password)
    return sum(int(digit) for digit in str(ascii_sum))

# Function to encrypt the message
def encrypt_message(message, pass_value):
    encrypted_message = []
    for word in message.split():
        if len(word) < 3:
            # Reverse the word and increment ASCII values by 2
            encrypted_word = ''.join(chr(ord(char) + 2) for char in reversed(word))
        else:
            # Reverse the word and add random characters equal to pass value
            reversed_word = word[::-1]
            random_chars = ''.join(chr(random.randint(33, 126)) for _ in range(pass_value))
            encrypted_word = reversed_word + random_chars
        encrypted_message.append(encrypted_word)
    # Append the pass value at the end of the message
    encrypted_message.append(str(pass_value))
    return ' '.join(encrypted_message)

# Main function to handle the encryption process
def main():
    # Input password
    while True:
        password = input("Enter an encrypted password (3-10 characters): ")
        if 3 <= len(password) <= 10:
            break
        print("Password must be between 3 and 10 characters.")

    pass_value = compute_password_value(password)

    # Input message
    message = input("Enter the message to encrypt: ")

    # Encrypt the message
    encrypted_message = encrypt_message(message, pass_value)

    # Get yesterday's date for filename
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    filename = yesterday.strftime("%Y-%m-%d") + ".txt"

    # Create diary folder if it doesn't exist
    os.makedirs("diary", exist_ok=True)

    # Save the encrypted message to the file
    file_path = os.path.join("diary", filename)
    with open(file_path, "w") as file:
        file.write(encrypted_message)

    print(f"Encrypted message saved to {file_path}")

if __name__ == "__main__":
    main()
