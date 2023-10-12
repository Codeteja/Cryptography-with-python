
alpha = "abcdefghijklmnopqrstuvwxyz"


def affine_enc(plaintext , key):
    ciphertext = ""
    plaintext = plaintext.lower()
    for i in plaintext:
        try:
            j = (key[0]*alpha.index(i) + key[1]) % 26
            ciphertext = ciphertext + alpha[j]
        except ValueError:
            ciphertext = ciphertext + i
    return ciphertext

def extended_gcd(a,b):
    if a == 0:
        return b , 0 , 1 
    else:
        gcd , x , y = extended_gcd(b % a ,a )
        return gcd, y - (b//a)*x , x

def mod_inverse(x):
    m = 26
    return x % m


def aff_dec(ciphertext , key):
    plaintext = ""
    m = 26
    x = (extended_gcd(key[0] , m)[1]) % m
    for i in ciphertext:
        try:
            j = (x * (alpha.index(i) - key[1])) % 26
            plaintext = plaintext + alpha[j]
        except ValueError:
            plaintext = plaintext + i
    return plaintext

message = "This is Tejas"
key = [3,5]

ciphertext = affine_enc(message , key)
plain = aff_dec(ciphertext , key)

print("Encrypted text is = " , ciphertext)
print("DEcrypted text is = " , plain)












plaintext = "This is tejas"
key = [3,5]
print(affine_enc(plaintext , key))

    
        