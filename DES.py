from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

# DES key 64 bits 

key = b'mysecret' # byte representation of the string
print(key)
# if key is more than 64 bits then we can do is that we took only first 64 bits of it

# DES will generate IV automatically
cipher = DES.new(key,DES.MODE_CBC)
print(cipher.block_size)
print(cipher.iv)

plaintext = b'This is a message'
# We have to make sure is that we want 64 bits blocks of the message so we need padding also 
print(pad(plaintext,DES.block_size)) # This dones the padding if needed of given DES blocksize
ciphertext = cipher.encrypt(pad(plaintext,DES.block_size))
iv = cipher.iv
print(ciphertext)

decrypt_cipher = DES.new(key,DES.MODE_CBC,iv)
original = decrypt_cipher.decrypt(ciphertext)
original = unpad(original,DES.block_size)
print(original.decode())