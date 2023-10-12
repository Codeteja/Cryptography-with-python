# python program to implement RSA + AES version of cryptosystem
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES , PKCS1_OAEP

# generate the keys
key = RSA.generate(2048)
private_key = key
public_key = key.public_key()

# RSA encryption
data = "This is just a simple message".encode()
print(data) 
# this is the private key in AES which 16 bytes
session_key = get_random_bytes(16) 
print(session_key)
# encrypt the session key with the public RSA key
# encryption --- public key
encrypt_rsa = PKCS1_OAEP.new(public_key)
enc_session_key = encrypt_rsa.encrypt(session_key)
# encrypted verison of session key which we send to the reciever
print(enc_session_key)

# we encrypt the data with AES
cipher_aes = AES.new(session_key,AES.MODE_GCM)
# digest is used for authentication
cipher_text , tag = cipher_aes.encrypt_and_digest(data)
print(cipher_text)
print(tag)
nonce = cipher_aes.nonce

# RSA decryption
decrypt_rsa = PKCS1_OAEP.new(private_key)
sess_key = decrypt_rsa.decrypt(enc_session_key)
print(sess_key) # match it with the session key above
decrypt_aes = AES.new(sess_key , AES.MODE_GCM , nonce)
plain_text = decrypt_aes.decrypt_and_verify(cipher_text,tag)
print(plain_text.decode())
