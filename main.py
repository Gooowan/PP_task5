import string


def encrypt(rawText, key):
    cipher = ""
    key = key % 26

    for char in rawText:
        if char.isalpha():
            alpha_start = ord('a') if char.islower() else ord('A')
            shift = (ord(char) - alpha_start + key) % 26
            cipher += chr(alpha_start + shift)
        else:
            cipher += chr(ord(char)+key)
    return cipher


def decrypt(cipher, key):
    rawText = ""
    key = key % 26

    for char in cipher:
        if char.isalpha():
            alpha_start = ord('a') if char.islower() else ord('A')
            shift = (ord(char) - alpha_start - key + 26) % 26
            rawText += chr(alpha_start + shift)
        else:
            rawText += chr(ord(char)-key)
    return rawText


a = encrypt("Hello, World!", 3)
print(a)
a = decrypt(a,3)
print(a)