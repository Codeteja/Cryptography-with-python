# python programme for finding gcd of 2 no
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
a = int(input("Enter the first no = "))
b = int(input("Enter the second no = "))
print("The gcd of given numbers is " , gcd(a,b))

