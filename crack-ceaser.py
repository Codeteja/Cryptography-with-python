# Python programme to crack the ceaser cipher using bruteforce
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#print(len(alphabet))

def ceaser_crack(ciphertext):
    # we try all possible key values
    for key in range(len(alphabet)):
        plaintext = ''
        for i in ciphertext.lower():
            try:
                j = (alphabet.index(i)- key) % 26
                plaintext = plaintext + alphabet[j]
            except ValueError:
                plaintext = plaintext + i # if the character is not from our alphabet add as it is
        print(f"The key is {key} and the plaintext is  {plaintext}")

ciphertext = input("Enter the message encrypted by ceaser cipher = ")    
ceaser_crack(ciphertext)