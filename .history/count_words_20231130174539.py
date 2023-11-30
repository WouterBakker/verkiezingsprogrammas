# Get word count for each party
import pickle

with open('dict_programmas_all.pkl', 'rb') as file:
    dict_programmas_all = pickle.load(file)

with open('dict_programmas_year.pkl', 'rb') as file:
    dict_programmas_year = pickle.load(file)
    


def count_words(text):
    word_counts = {}
    # Split the text into words
    words = text.split()
    for word in words:
        # Remove punctuation and convert to lowercase for better counting
        cleaned_word = word.strip('.,!?()"\'').lower()
        # Update the count in the dictionary
        if cleaned_word in word_counts:
            word_counts[cleaned_word] += 1
        else:
            word_counts[cleaned_word] = 1
    return word_counts

## Count number of times each word is used in partijprogramma
dict_wordcounts = {}

for key, item in dict_programmas_all.items():
    counted_words = count_words(item) #saves as dictionary
    sorted_words = dict(sorted(counted_words.items(), key=lambda x: x[1], reverse=False)) #saves as tuple, so convert to dictionary
    dict_wordcounts[key] = sorted_words


d

