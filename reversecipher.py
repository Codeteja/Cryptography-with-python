# python programme for a reverse cipher

# encryption function
def reverse_cipher(plaintext):
    ciphertext = '' # defining ciphertext to be empty string initially
    i = len(plaintext)-1
    while i>=0:
        ciphertext = ciphertext + plaintext[i]
        i = i-1
    return ciphertext

# Taking input from user
plaintext = input("Enter the text you want to encrypt "  )


ciphertext = reverse_cipher(plaintext)
print("Enrypted text is : ",ciphertext)

# decryption function
def decrypt_reverse(ciphertext):
    originaltext = ''
    i = len(ciphertext)-1
    while i>=0:
        originaltext = originaltext + ciphertext[i]
        i = i-1
    return originaltext
decrypted_text = decrypt_reverse(ciphertext)
print("Decrypted text is ",decrypted_text)