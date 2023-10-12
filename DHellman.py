# python programme to implement the Diffie-Hellman key-exchange protcol
import random

def generate_private_key(n,g):
    # Alice public key exponent 
    x = random.randint(1,n)
    # Bob public key exponent
    y = random.randint(1,n)

    # Public key of Alice g^x
    k1 = pow(g,x) % n
    # Public key of Bob g^y
    k2 = pow(g,y) % n

    # private key for encryption is follows
    print("Alice private key is = ", pow(k2,x,n))
    print("Bob private key is = ", pow(k1,y,n))


generate_private_key(17,3)