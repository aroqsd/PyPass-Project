import base64

def caesar_encrypt(text, shift):
    cipher = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            cipher += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher += char
    return cipher

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def base64_encrypt(text):
    message_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_text = base64_bytes.decode('ascii')
    return base64_text

def base64_decrypt(text):
    base64_bytes = text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message_text = message_bytes.decode('ascii')
    return message_text

print("Choose the operation you want to perform:")
print("1. Encryption")
print("2. Decryption")
print("Please make your selection: ")

choice = input()

if choice == '1':
    plaintext = input("Please enter the text to be encrypted: ")
    shift = int(input("Please enter the shift amount for Caesar encryption: "))
    filename = input("Please enter the name of the file: ")
    ciphertext = caesar_encrypt(plaintext, shift)
    ciphertext = base64_encrypt(ciphertext)
    with open(filename + '.txt', 'w') as file:
        file.write('Account name: ' + filename + '\n')
        file.write('Password: ' + ciphertext)
        file.close()
    print("Encrypted text successfully saved to file!")
    
elif choice == '2':
    filename = input("Please enter the name of the file: ")
    with open(filename + '.txt', 'r') as file:
        lines = file.readlines()
        ciphertext = lines[1][10:]
        shift = int(input("Please enter the shift amount for Caesar decryption: "))
        ciphertext = base64_decrypt(ciphertext)
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print("Decrypted text: ", decrypted_text)
        input("Press enter to close the console window...")
    
else:
    print("Invalid choice!")
    input("Press enter to close the console window...")
