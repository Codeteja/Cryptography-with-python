# python code for Implementation of substitution cipher
# caesaer cipher is the special version of substitution cipher

key = 'abcdefghijklmnopqrstuvwxyz'

def caeser_enc(n,plaintext):
    result = ''
    for i in plaintext.lower():
        # try tries to find the index of char of plaintext in key and if a char has no match in key then valueerror is occured
        try:
            j = (key.index(i) + n) % 26
            result = result + key[j]
        except ValueError:
            result = result + i
    return result


def caeser_dec(n,ciphertext):
    plaintext = ''
    for i in ciphertext.lower():
            try:
                 j = (key.index(i) - n) % 26
                 plaintext = plaintext + key[j]
            except ValueError:
                 plaintext = plaintext + i
    return plaintext


plain = input("Enter the data to encrypt using caesar cipher = ")
n = int(input("Enter the shift value = "))

ciphertext = caeser_enc(n,plain)

print("Ciphertext : ", ciphertext)

plaintext = caeser_dec(n,ciphertext)

print("Plaintext : ", plaintext)


