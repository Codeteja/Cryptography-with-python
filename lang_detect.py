# python programme for detection of english langauge
# we make a dict of english words and use it

English_words = []

def get_data():
    dictionary = open('englishwords.txt' , 'r')

    # initialize the English_words list with the words present in the file
    # every word is in the distinct line in the file so we have to use split('\n')
    for word in dictionary.read().split('\n'):
        #print(word)
        English_words.append(word)

    dictionary.close()

    print(len(English_words))

def count_words(text):
        # upper case letters are needed 
    text = text.upper()
        # transform text into list splitted by spaces
    words = text.split(' ')
        # matches counts the no of english words in the text
    matches = 1

        # Checks the word is present in the dictionary/english or not
    for word in words:
        if word in English_words:
            matches = matches + 1
    return matches


def is_text_english(text):
    matches = count_words(text)
    # formula to accept the text based on matches
    if(float(matches)/ len(text.split(' ')))*100 >= 50:
        return True
    else:
        return False


get_data()
plain_text = input("Enter the text = ")
print(is_text_english(plain_text))


