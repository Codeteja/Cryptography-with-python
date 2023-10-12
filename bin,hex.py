# python code for binary and hexadecimal conversions

# binary conversion is done using bin()

import binascii
import codecs
import string


a = 60
print(bin(a))
b = 6
print(bin(b))
print(bin(a ^ b))  # ^ denotes the bitwise xor operator
print(bin(~a))  # binary one's compliment
print(bin(a<<2))  # binary left shift
print(bin(a>>2)) # binary right shift

# encode method on strings

#string to its hexadecimal conversion
string = "Hello World"
hex_string = string.encode().hex()
print(hex_string)

# convert hex to integers
int_string = int(hex_string,16)
print(int_string)

# convert integer back to hex
bak2hex = format(int_string,'x')
print(bak2hex)

# convert back to string
string = bytes.fromhex(bak2hex).decode() # fromhex convert hexadecimal to bytes and then decode() convert these to original string
print(string)

string2 = "Tejas"

binary_conversion= string2.encode() # converting to bytes

# convert to hex using binascii() and hexlify()
hexstring = binascii.hexlify(binary_conversion)
print(hexstring)

string = binascii.unhexlify(hexstring)
print(string)



