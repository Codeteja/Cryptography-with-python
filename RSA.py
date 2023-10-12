#Python Programme to implement RSA encryption
import random
from math import floor
from math import sqrt
Random_start = 1000
Random_end = 100000
# We are going to generate prime no withing above range

# now we check the generated num is prime or not

def is_prime(num):
    if num<2:
        return False
    if num==2:
        return True
    if(num %2 ==0):
        return False
    for i in range(3 , floor(sqrt(num)) ):
        if num % i ==0:
            return False
    return True

# now we find gcd of 2 integers for the step (e,phi(n)) = 1 or not
def gcd(a,b):
    if(a%b == 0):
        return b
    else:
        return gcd(b,a%b)
    
# now we have to find the modular inverse since we need to find d such that e.d = 1 mod(phi(n))
# we use Extended eulidean algorithm as it has linear time complxity
def modular_inverse(a,b):
    if a==0:
        return b,0,1
    div,x1,y1 = modular_inverse(b % a, a)

    x = y1 - (b//a)*x1
    y = x1

    return div , x, y

# now we generate random prime no
def generatelarge_primes(start = Random_start , end = Random_end):
    num = random.randint(start,end)

    while not is_prime(num):
        num = random.randint(start,end)

    return num

# now we generate RSA keys
def generate_rsa_keys():
    # generate huge prime no
    p = generatelarge_primes()
    q = generatelarge_primes()

    # Integer used in the algorithm which is a trapdoor function
    n = p*q
    # Euiler phi function of n
    phi = (p-1) * (q-1)

    # now we have to find e such that (e,phi(n)) = 1
    e = random.randrange(1,phi)
    while gcd(e,phi) !=1:
        e =random.randrange(1,phi)
    
    # now we have to find the modular inverse d of e such that e.d = 1 mod(phi(n))
    d = modular_inverse(e,phi)[1]

    # now we can very well give the private and public keys
    return (d,n) , (e,n)

# Now we define encryption function
def encrypt_rsa(public_key , plaintext):
    e,n = public_key
    # it is a list of each char gets exponianted and then go modulo n
    ciphertext = []
    for char in plaintext:
        a = ord(char) # convert char into numerical ASCII value
        ciphertext.append(pow(a,e,n)) # pow(a,e,n) = a^e mod(n)
    return ciphertext

# Now we define decryption function
def decrypt_rsa(private_key , ciphertext):
    d,n = private_key
    plaintext = ''

    for num in ciphertext:
        a= pow(num, d, n)
        plaintext = plaintext + str(chr(a)) #chr(a) gives the character represent of num a an str is used to add it to string plaintext
    return plaintext


if __name__== '__main__':
    private_key , public_key = generate_rsa_keys()
    message = input("Enter the data to encrypt using RSA cryptosystem = ")
    print("Entered data is = " , message)
    cipher = encrypt_rsa(public_key , message)
    print("Cipher text is ", cipher)
    plain = decrypt_rsa(private_key , cipher)
    print("Decrypted text is ", plain)