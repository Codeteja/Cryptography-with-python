# python programme to implement MD5 hashing algorithm
# MD5 is 125bit hash
# By the birthday paradox it is not secure for collision

from hashlib import md5

message = b'My name is Tejas'
result = md5(message)
print(result.hexdigest())
print(result.digest())
