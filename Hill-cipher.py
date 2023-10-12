# python programme for implementation of 2 by 2 Hill cipher
import sys
import numpy as np

# Encryption function

def hill_enc(plaintext , key):
    # if message length is an odd no place a zero at the end
    len_chek = 0
    if(len(plaintext) % 2 != 0):
        plaintext = plaintext + "0"
        len_chek = 1

    # convrsion of message to hill matrix
    row = 2
    col = int(len(plaintext)/2)
    # This creates a zero matrix of given dimmenssion
    msg2d = np.zeros((row,col),dtype =int)

 # below code creates a matrix with even index entries in 1st row and odd no in 2nd
    itr1 = 0
    itr2 = 0
    for i in range(len(plaintext)):
        if(i%2 ==0):
            msg2d[0][itr1] = int(ord(plaintext[i]) - 65)
            itr1 = itr1 + 1
        else:
            msg2d[1][itr2] = int(ord(plaintext[i]) - 65)
            itr2 = itr2 + 1
    print(msg2d)
        
    # key to 2 by 2 matrix 
    key2d = np.zeros((2,2) , dtype = int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = int(ord(key[itr3]) - 65)
            itr3 = itr3 + 1
    print(key2d)


    # Checking validity of the key
    # finding determinant of key matrix
    def determinant(matrix):
        det = ((matrix[0][0] * matrix[1][1]) - matrix[0][1] * matrix[1][0])
        return det

    det_key = determinant(key2d)
    print("determinant is",det_key)

    # Finding multiplicative inverse of determinat modulo 26
    mul_inv = -1
    for i in range(26):
        inv = det_key * i
        if(inv % 26 == 1):
            mul_inv = i
            break
        else:
            continue

    if mul_inv == -1 :
        print("Invalid key")
        sys.exit()
    print("multiplicative inverse is ",mul_inv)


    encrypt_text =""
    # This multiplication of matrix is done such that ciphertext is added in proper sequence
    itr_count = int(len(plaintext)/2)
    if(len_chek == 0):
        for i in range(itr_count):
            temp1 = msg2d[0][i]*key2d[0][0]  + msg2d[1][i]*key2d[0][1]
            encrypt_text = encrypt_text + chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i]*key2d[1][0] + msg2d[1][i]*key2d[1][1]
            encrypt_text = encrypt_text + chr((temp2 % 26) + 65)
    else:
        for i in range(itr_count - 1):
            temp1 = msg2d[0][i]*key2d[0][0]  + msg2d[1][i]*key2d[0][1]
            encrypt_text = encrypt_text + chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i]*key2d[1][0] + msg2d[1][i]*key2d[1][1]
            encrypt_text = encrypt_text + chr((temp2 % 26) + 65)  
    
    print("Encrypted text : {}".format(encrypt_text))
    return encrypt_text


# Decryption function

# This almost follow on the same lines the only thing is we have to find the inverse of the key matrix

def hill_dec(ciphertext , key):

    # check for cipher message length for padding or not
    len_chek = 0
    if(len(ciphertext) % 2 !=0):
        ciphertext = ciphertext + "0"
        len_chek = 1

    # ciphertext to matrix
    row = 2 
    col = int(len(ciphertext)/2)
    cip2d = np.zeros((row,col) , dtype = int)

    itr1 = 0
    itr2 = 0
    for i in range(len(ciphertext)):
        if(i % 2 == 0):
            cip2d[0][itr1] = int(ord(ciphertext[i]) - 65)
            itr1 = itr1 + 1
        else:
            cip2d[1][itr2] = int(ord(ciphertext[i]) - 65)
            itr2 = itr2 + 1
    
    print(cip2d)
    
    # key to 2*2 matrix
    key2d = np.zeros((2,2) , dtype = int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = int(ord(key[itr3]) - 65)
            itr3 = itr3 + 1
    
    print(key2d)
    
    # finding determinant
    def determinant(matrix):
        det = ((matrix[0][0] * matrix[1][1]) - matrix[0][1] * matrix[1][0])
        return det

    det_key = determinant(key2d)
    print("determinant is",det_key)

    # Finding multiplicative inverse of determinat modulo 26
    mul_inv = -1
    for i in range(26):
        inv = det_key * i
        if(inv % 26 == 1):
            mul_inv = i
            break
        else:
            continue

    if mul_inv == -1 :
        print("Invalid key")
        sys.exit()
    
    print("Multiplicative inverse",mul_inv)
    

    # Inverse of a 2 by 2 key matrix 
    # First find adjoint matrix which is simple in case of 2
    # swapping 
    key2d[0][0] , key2d[1][1] = key2d[1][1] , key2d[0][0]

    key2d[0][1] = (key2d[0][1]*(-1))
    key2d[1][0] = (key2d[1][0]*(-1))
    
    # modulo
    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26
  
    print("Adjoint matrix of key2d",key2d)
  
    # multiplying by inverse of determinant
    for i in range(2):
        for j in range(2):
            key2d[i][j] = mul_inv * key2d[i][j]
            
    # modulo
    for i in range(2):
      for j in range(2):
        key2d[i][j] = key2d[i][j] % 26
        
    print("invers of key2d",key2d)
        
    
    # ciphertext to plaintext
    decryption = ""
    itr_count = int(len(ciphertext)/2)
    if(len_chek == 0):
      for i in range(itr_count):
        temp1 = cip2d[0][i]*key2d[0][0]  + cip2d[1][i]*key2d[0][1]
        decryption = decryption + chr((temp1 % 26) + 65)
        temp2 = cip2d[0][i]*key2d[1][0] + cip2d[1][i]*key2d[1][1]
        decryption = decryption + chr((temp2 % 26) + 65)
    else:
      for i in range(itr_count - 1):
        temp1 = cip2d[0][i]*key2d[0][0]  + cip2d[1][i]*key2d[0][1]
        decryption = decryption + chr((temp1 % 26) + 65)
        temp2 = cip2d[0][i]*key2d[1][0] + cip2d[1][i]*key2d[1][1]
        decryption = decryption + chr((temp2 % 26) + 65)
            
    
    print("Decrypted text : {}".format(decryption))
    return decryption




        
        
plaintext = "Secret Message"
plaintext = plaintext.upper().replace(" ","")
key = "hill"
key = key.upper().replace(" ","")
ciphertext = hill_enc(plaintext,key)
print("Ciphertext is :",ciphertext)
original = hill_dec(ciphertext ,key)
print("Original text = " , original)





