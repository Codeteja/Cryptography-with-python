# python programme to implememnt integer factorization

def get_factors(n):
    factors = []
    count = 0
    for d in range(1,n-1):
        if(n % d == 0):
            count = count + 1
            factors.append([d,n/d])
    print("No of factors is " , count*2)
    return factors

n = int(input("Enter the no to find the factorizatio = "))
print(get_factors(n))