# python programme for the implementation of vigenere cipher

# we define a key_array of given key first

# key function 

def key_vigenere(key):
    key = key.upper()
    key_array = []
    for i in range(0,len(key)):
        # below step is like translate from set 65-91 to 0-25 set
        key_element = (ord(key[i]) - ord('A')) % 26    # ord(A) = 65
        key_array.append(key_element)
    #print(key_array)
    return key_array

# shift function

def shift_enc(c,n):
    return chr(((ord(c) - ord('A')) + n) % 26 + ord('A'))

def shift_dec(c,n):
    return chr(((ord(c) - ord('A')) - n) % 26 + ord('A'))

# Encryption function

def enc_vigenere(plaintext,key):
    
    plaintext = plaintext.upper()
    
    ciphertext =''
    
    for i in range(0,len(plaintext)):
        
        c_letter = shift_enc(plaintext[i],key[i % len(key)])
        
        ciphertext = ciphertext + c_letter

    return ciphertext

# Decryption function

def dec_vigenere(ciphertext , key):
    plaintext = ''

    for i in range(0,len(ciphertext)):

        p_letter = shift_dec(ciphertext[i],key[i % len(key)])

        plaintext = plaintext + p_letter

    return plaintext



secret_key = input("Enter the key = ")

secret_key = secret_key.replace(" ","")

key  = key_vigenere(secret_key)

print(key)


plain = input("Enter the data to encrypt = ")

plain = plain.replace(" ","") # to remove blank spaces

print(plain)

ciphertext = enc_vigenere(plain , key)

print("Cipher text is : ", ciphertext)


plaintext = dec_vigenere(ciphertext,key)

print("Plaintext is = ", plaintext)