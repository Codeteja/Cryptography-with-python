# Python programme to implement dicrete log problem
# a = b^c(mod(m))
def modular_expo(b,c,m):
    return pow(b,c) % m

def discrete_log(a,b,m):
    c = 1
    while(pow(b,c) % m !=a):
        c = c+1
    return c


print(modular_expo(5,3,17))
print(discrete_log(6,5,17))