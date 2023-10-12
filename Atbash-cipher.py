# python programme to implement special version of substitution cipher called Atbash cipher
# Atbash cipher is substitution of char to char directly 

''' First we make a character mapping dictionary
char_map = {'A':'Z', 'B':'Y', 'C':'X', 'D':'W' , 'E':'V' , 'F':'U' , 'G':'T', 'H':'S', 'I':'R', 'j':'Q', 'K':'P',
             'L':'O' , 'M':'N', 'N':'M', 'O':'L', 'P':'K', 'Q':'J' , 'R':'I' , 'S':'H', 'T':'G' , 'U':'F' , 'V':'E' , 
            'W':'D','X':'C','Y':'B','Z':'A' } '''

# encryption of atbash cipher
def atbash(text):
    result =''
    character_set = list(text.upper())
    for character in character_set:
        if character in char_map:
            result = result + char_map.get(character)
        else:
            result = result + character
    return result

# Observe that decryption happens exactly same as cha_map is bijective in nature


# Another way to create the dictionary of above cha_map is

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
reverse_alphabet = list(reversed(alphabet))
char_map = dict(zip(alphabet,reverse_alphabet))
print(char_map)



plain = input("Enter the data to encrypt using atbash cipher = " )
print("Plaimtext is :" , plain)

ciphertext = atbash(plain)
print("Ciphertext is : " , ciphertext)

