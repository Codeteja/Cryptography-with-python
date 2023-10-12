# python programe for random no generator and exhaustive search using looping

import random
# generate a random password
generated_password = int(random.randint(0,9999)) # we can use str also to pick a string in this range

# loop for checking all values with generated_password
for i in range(0,10000):
   # trial = str(i) # if str is used above then this line converts i to str
    if i == generated_password:
        print("Password found ", generated_password)

        