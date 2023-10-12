# python programme to implement SHA-512 hash

from hashlib import sha512

m1 = "This is the message"

result = sha512(m1.encode())

print(result.hexdigest())