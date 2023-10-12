# we can choose a random key of length that of message
import secrets

# secrets.randbelow() is choose random no from 0 to given argument into brackets
a = secrets.randbelow(10)
print(a)

msg = "Hello World"
key =''
for i in range(len(msg)):
    # secrets.choice() is choose a character from the input to the brackets so we loop upto msg len
    key = key + secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

print(key)
print("length of msg " , len(msg))
print("length of randomly generated key ",len(key))
