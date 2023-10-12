# python function to find euiler phi function

import math
def phi(n):
    total = 0
    for i in range(1,n+1):
        if(math.gcd(i,n) == 1):
            #print(i)
            total = total + 1
    return total

for n in range(1,20):
    print(f"Euiler phi function of {n} = ",phi(n))