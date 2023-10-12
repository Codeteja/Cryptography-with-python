# python programme to implement SHA-256 hash
# This is 256 bit hash
# This is used in blockchain technology mainly in bitcoin blockchain
# The output is 64 hexadecimal characters
# each hexadecimal character is 4 bits therefore total 256 bits
# The collision in this is with extremely low probabilty
from hashlib import sha256

m1 = "Hello I am Tejas"
# to see the avalanche effect we slightly change the above message
m2 = "Hello I a Tejas"

result1 = sha256(m1.encode())
result2 = sha256(m2.encode())


print(result1.hexdigest())
print(result2.hexdigest())

