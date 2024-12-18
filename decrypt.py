import os

# Function to compute the password value
def compute_password_value(password):
    ascii_sum = sum(ord(char) for char in password)
    return sum(int(digit) for digit in str(ascii_sum))

# Function to decrypt the message
def decrypt_message(encrypted_message, pass_value):
    parts = encrypted_message.split()
    if not parts:
        raise ValueError("The file is empty or corrupted.")

    # Extract the pass_value at the end
    file_pass_value = int(parts[-1])
    if file_pass_value != pass_value:
        raise ValueError("Password does not match.")

    decrypted_message = []
    for word in parts[:-1]:
        if len(word) > pass_value:  # Words with appended random characters
            # Strip random characters and reverse the rest
            word_without_random = word[:-pass_value]
            decrypted_word = word_without_random[::-1]
        else:  # Words with less than 3 characters
            # Reverse the word and decrement ASCII values by 2
            reversed_word = word[::-1]
            decrypted_word = ''.join(chr(ord(char) - 2) for char in reversed_word)
        decrypted_message.append(decrypted_word)

    return ' '.join(decrypted_message)

# Main function to handle the decryption process
def main():
    diary_folder = "diary"
    if not os.path.exists(diary_folder):
        print("No diary folder found. Make sure to encrypt a message first.")
        return

    files = [f for f in os.listdir(diary_folder) if f.endswith(".txt")]
    if not files:
        print("No files found in the diary folder.")
        return

    print("Available files:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")

    while True:
        try:
            choice = int(input("Enter the number of the file you want to decrypt: "))
            if 1 <= choice <= len(files):
                selected_file = files[choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid file number.")
        except ValueError:
            print("Please enter a number.")

    file_path = os.path.join(diary_folder, selected_file)

    while True:
        password = input("Enter the password: ")
        if 3 <= len(password) <= 10:
            pass_value = compute_password_value(password)
            break
        print("Password must be between 3 and 10 characters.")

    try:
        with open(file_path, "r") as file:
            encrypted_message = file.read()
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    try:
        decrypted_message = decrypt_message(encrypted_message, pass_value)
        print("Decrypted message:")
        print(decrypted_message)
    except ValueError as e:
        print(f"Decryption failed: {e}")

if __name__ == "__main__":
    main()
