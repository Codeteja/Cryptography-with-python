# python programme for implementation of Fermats little theorem
# Fermats litle theorem =
# if p is prime then for all  a such that
# 0 < a < p
# a^(p-1) = 1 mod(p)
def FLT(n):
    if (n==1):
        return False
    else:
        for a in range(1,n):
            if(pow(a,n-1,n) != 1):
                return False
        return True

n = int(input("Enter the no to check for primality using FLT = "))        
print(FLT(n))

# FLT to find modular inverse modulo prime

def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
def mod_inverse(a,p):
    if(gcd(a,p) != 1):
        print("Inverse does not exist")
    else:
        print("multiplicative inverse modulo p is = ")
        return pow(a,p-2,p)

a = int(input("Enter the no to find modular inverse = "))
p = int(input("Enter the prime modulus"))
print(mod_inverse(a,p))


