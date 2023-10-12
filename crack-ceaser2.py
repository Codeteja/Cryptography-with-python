# In this we crack the ceaser cipher using the frequency analysis 
import matplotlib.pylab as plt
# whitespace is also most frequent letter in english

LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequency_analysis(text):
    text = text.upper()
    # we make dictionary of letters and add occurences of letters in it for given text
    letter_frequencies = {}

    for letter in LETTERS:
        letter_frequencies[letter] = 0
    #print(letter_frequencies) # upto this step dict is created with each letter-freq = 0
    
    # Now we analyise text and add that no of occurence of letter to dictionary
    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] = letter_frequencies[letter] + 1
    #print(letter_frequencies) # this will complete the frequence updation in dict
    return letter_frequencies   

    # we plot the bar graph
def plot_distributions(letter_frequencies):
    plt.bar(letter_frequencies.keys() , letter_frequencies.values())
    plt.show()

def crack_ceaser(ciphertext):
    freq = frequency_analysis(ciphertext) # returns the dictionary with frequencies of letters
    #plot_distributions(freq)
    # This will sort dict in the values in descending order
    freq = sorted(freq.items(), key=lambda x:x[1], reverse= True)
    print(freq)
    # since blank space is also considerd in the letter we go modulo 27
    print ("The possible value of key is = ",(LETTERS.index(freq[0][0]) - LETTERS.index('E')) % 27)

ciphertext = input("Enter the input cipher text to find the key in ceaser encryption = ")
crack_ceaser(ciphertext)