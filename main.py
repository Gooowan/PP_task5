def encrypt_char(char, key):
    if char.isalpha():
        alpha_start = ord('a') if char.islower() else ord('A')
        return chr((ord(char) - alpha_start + key) % 26 + alpha_start)
    else:
        return chr(ord(char)+key)


def encrypt(rawText, key):
    return ''.join([encrypt_char(char, key) for char in rawText])


def decrypt_char(char, key):
    if char.isalpha():
        alpha_start = ord('a') if char.islower() else ord('A')
        return chr((ord(char) - alpha_start - key + 26) % 26 + alpha_start)
    else:
        return chr(ord(char)-key)


def decrypt(cipher, key):
    return ''.join([decrypt_char(char, key) for char in cipher])


def read_from_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def write_to_file(file_name, text):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text written to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    buffer = ""
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        print("4. Read from file")
        print("5. Write to file")
        choice = input("Enter your command: ")

        if choice == "1":
            rawText = input("Enter the text to encrypt or 'r' to use the text from the last read file: ")
            key = int(input("Enter the key: ")) % 26
            if rawText.upper() == 'r':
                buffer = encrypt(buffer, key)
            else:

                buffer = encrypt(rawText, key)
                print("Encrypted text: " + buffer)

        elif choice == "2":
            cipher = input("Enter the text to decrypt or 'r' to use the text from the last read file: ")
            key = int(input("Enter the key: ")) % 26
            if cipher.upper() == 'r':
                buffer = decrypt(buffer, key)
            else:
                buffer = decrypt(cipher, key)
                print("Decrypted text: " + buffer)

        elif choice == "3":
            file_name = input("Enter the file name to read from: ")
            text = read_from_file(file_name)
            if text is not None:
                buffer = text
                print("Text read from file.")

        elif choice == "4":
            if not buffer:
                print("No text available to write. Please encrypt or decrypt some text first.")
                continue
            file_name = input("Enter the file name to write to: ")
            write_to_file(file_name, buffer)

        elif choice == "5":
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
