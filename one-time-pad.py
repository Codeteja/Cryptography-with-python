# python programme for one time pad
from binascii import hexlify,unhexlify

# encryption function
def otp_encrypt(plaintext,key):
    ciphertext = ''

    # first convert to binary
    plaintext = plaintext.encode()
   # key = key.encode()

    # First convert both to hexadecimal
    hex_plain = hexlify(plaintext)
    #hex_key = hexlify(key)

    # Convert hexadecimal to the integer form
    plain_int = int(hex_plain,16)
    #key_int = int(hex_key,16)

    # Now we are ready to do the xor operation on these integer forms of plaintext and key
    ciphertext = plain_int ^ key
    return ciphertext

def otp_decrypt(ciphertext,key):
    msg = ciphertext ^ key

    # convert the msg to hexadecimal
    hex_msg = format(msg,'x')
    # convert this hexadecimal back to string format using unhexlify
    plaintext = unhexlify(hex_msg)
    return plaintext

def otp_key(a):
    print("Enter the key with length greater than or equal to" , a)
    key = str(input("Enter your key of specified lenght = "))
    if(len(key) >= a):
        print("Key accepted")
        key = key.encode()
        hex_key = hexlify(key)
        int_key = int(hex_key,16)
        return int_key
    
    else:
        print("lenght of key is :",len(key))
        print("rejected")

    
plain = str(input("Enter the message to encrypt = " ))

a = len(plain)

key = otp_key(a)

ciphertext = otp_encrypt(plain,key)

print("ciphertext is :" , ciphertext)

plaintext = otp_decrypt(ciphertext,key)

print("plaintext is :", plaintext)




