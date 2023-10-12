# python function to implement the affine cipher

def mod26shift(c):
    letter = ord(c) - ord('A')
    return letter

def aff_enc(plaintext,key):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ","")
    ciphertext = ''
    for i in range(len(plaintext)):
        word = chr((key[0]*(mod26shift(plaintext[i])) + key[1]) % 26 + ord('A'))
        ciphertext = ciphertext + word
    return ciphertext

# For decryption purpose we need to find inverse of a using extended euclidean algorithm
def aff_dec(ciphertext , key):
    ciphertext = ciphertext.upper()
    plaintext = ''
    inverse = d
    for i in range(len(ciphertext)):
        word = chr((inverse*(mod26shift(ciphertext[i]) - key[1]) % 26 ) + ord('A'))
        plaintext = plaintext + word
    return plaintext

# Extended euclidean algorithm
def extended_gcd(a,b):
    if a == 0:
        return b , 0 , 1 
    else:
        gcd , x , y = extended_gcd(b % a ,a )
        return gcd, y - (b//a)*x , x

# inverse of element modulo m
def mod_inverse(x):
    m = 26
    return x % m



plaintext = input("Enter the data for encryption = ")

key_input = input("Enter a list key elements: ")
key = eval(key_input)

a = key[0]
b = 26

c = extended_gcd(a,b)

if(c[0]!= 1):
    print("Invalid key: please modify the first element of the key")
  
else:
    d  = mod_inverse(c[1])
    ciphertext = aff_enc(plaintext,key)
    print("ciphertext = " , ciphertext)
    plaintext = aff_dec(ciphertext , key)
    print("plaintext = :",plaintext)


 
