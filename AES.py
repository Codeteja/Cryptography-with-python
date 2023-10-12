# We implement AES CBC mode 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

# private key of AES
# key must be 128bits or 16bytes
#key = get_random_bytes(16)  # generate random 16bytes
key = b'mysecretpassword' # this contains 16 bytes

cipher = AES.new(key,AES.MODE_CBC)
iv = cipher.iv
#print(iv)

plaintext = b'This is a message'
#print(pad(plaintext,AES.block_size))

ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))
print(ciphertext)

decrypt_cipher = AES.new(key,AES.MODE_CBC,iv)
originaltext = unpad(decrypt_cipher.decrypt(ciphertext),AES.block_size)

print(originaltext.decode())
