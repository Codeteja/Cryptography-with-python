# encryption and decryption using xor

import binascii

def xorKey(secret):
    # convert to binary(bits)
    secret = secret.encode()
    print(secret) 

    # converting to hexadecimal
    hexkey = binascii.hexlify(secret)

    # converting to integer
    key = int(hexkey,16) 

    print("Key :", key)
    return key

def xorEnc(msg,key):
    print("Message to encrypt ", msg)
    msg = msg.encode()
    hexmsg = binascii.hexlify(msg)
    print("hexmsg : ", hexmsg)
    ciphertext = int(hexmsg,16) ^ key
    print("Ciphertext : ", ciphertext)
    return ciphertext

def xorDec(ciphertext,key):
    msg =ciphertext ^ key
    bak2hex = format(msg,'x')
    print("bak2hex :",bak2hex)
    plaintext = binascii.unhexlify(bak2hex)
    print("plaintext :",plaintext)
    return plaintext

key = xorKey("rand")
cipher = xorEnc('Hello World',key)
plain = xorDec(cipher,key)
