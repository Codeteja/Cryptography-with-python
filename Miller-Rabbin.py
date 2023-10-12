# python programme to implement the miller rabbin test for primality

import random

# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2^r = n-1
# for some r >= 1
def millertest(d,n):

    # pick a random no in [2,n-2]
    # corner cases make sure that n>4
    a = 2 + random.randint(1,n-4)

    # compute a^d mod n
    x = pow(a,d,n)

    if(x == 1 or x == n-1):
        return True
    
    # if above fails then we do the following
    # 1) repeated squaring of x till we get -1 or +1 
    # 2) we find x^(2j) where j runs from 1 to r-1
    # following code is slightly in different lines but o/p is same
    while(d != n-1):
        x = (x*x) % n
        d = d*2  # this increment actually yeild r as power of 2 is multiplied to d 
        if(x == 1):
            return False
        if(x == n-1):
            return True
    # return composite
    return False

    # It returns false if n is
    # composite and returns true if n
    # is probably prime. k is an
    # input parameter that determines
    # accuracy level. Higher value of
       # k indicates more accuracy.
def isPrime( n, k):
     
    # Corner cases
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
 
    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
 
    # Iterate given number of 'k' times
    for i in range(k):
        if (millertest(d, n) == False):
            return False;
 
    return True;
 
# Number of iterations
k = 4;
 
print("All primes smaller than 100: ");
for n in range(1,100):
    if (isPrime(n, k)):
        print(n , end=" ");

