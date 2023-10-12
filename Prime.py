# python programme for checking prime no or not

def is_prime(x):
    x = abs(int(x))
    if(x<2):
        print("Less than 2")
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for n in range(3 , int(x**(0.5))+2 , 2):
            if(x % n == 0):
                return False
            else:
                return True 

x = int(input("Enter the no = "))
print("Is the given no prime ",is_prime(x))


