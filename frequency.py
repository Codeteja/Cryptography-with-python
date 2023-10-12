# python programme for implememntation of frequency analysis of letter
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
    




text = input("Enter the text to analyse the frequency analysis of the letters ") 
freq = frequency_analysis(text)
plot_distributions(freq) 