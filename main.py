import string


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


def main():
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        print("Enter your command: ", end="")
        choice = input()
        if choice == "1":
            print("Enter the text to encrypt: ", end="")
            rawText = input()
            print("Enter the key: ", end="")
            key = int(input())
            print("Encrypted text: ", end="")
            print(encrypt(rawText, (key % 26)))
        elif choice == "2":
            print("Enter the text to decrypt: ", end="")
            cipher = input()
            print("Enter the key: ", end="")
            key = int(input())
            print("Decrypted text: ", end="")
            print(decrypt(cipher, (key % 26)))
        elif choice == "3":
            break
        else:
            print("Invalid command")
            continue


if __name__ == "__main__":
    main()