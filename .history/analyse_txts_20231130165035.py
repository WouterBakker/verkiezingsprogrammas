import os
import pandas as pd
import spacy
nlp = spacy.load('nl_core_news_sm')

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the entire content of the file
        output = file.read().replace('\n', ' ')
    yield output

txts = os.listdir("programmas_txt")

dict_programmas_all = {}
dict_programmas_year = {}

for txt in txts:
    try:
        party, year = txt.split("_")
        year = year[:-4]
        if not party in dict_programmas_all:
            dict_programmas_all[party] = str()
            dict_programmas_year[party] = {}
        
        file_path = f"programmas_txt/{txt}"
        
        for programma in read_txt(file_path):
            dict_programmas_all[party] = dict_programmas_all[party] + " " + programma
            dict_programmas_year[party][year] = programma
            
    except Exception as e:
        print(f"caught exception: {e} for file {txt}")
    
# Get word count for each party

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


## Categorize the words with spacy
# Process the text with spaCy

# pvv_counts = dict_wordcounts['PVV']
# pvv_text = dict_programmas_all["PVV"]

# doc = nlp.pipe(pvv_text)

# words_pos = {x.text: x.pos_ for x in doc}

# for key, item in words_pos.items():
#     print(f"{key}: {item}")
    
    
#sentiment analysis
from textblob import TextBlob
from textblob_nl import PatternTagger, PatternAnalyzer

def get_sentiment(dict_programmas_year):
    '''
    Takes input dictionary of verkiezingsprogrammas from Parties:year:programma, 
    outputs dictionary of Parties:year:sentiment
    '''
    dict_sentiment = {}
    for party, programmas in dict_programmas_year.items():
        dict_sentiment[party] = {}
        for year, programma in programmas.items():
            dict_sentiment[party][year] = TextBlob(programma, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer()).sentiment
            
    return(dict_sentiment)
     
     
     
import matplotlib.pyplot as plt
dict_party_sentiment = get_sentiment(dict_programmas_year)




df = pd.DataFrame(dict_party_sentiment["GroenLinks"]).T.sort_index()
# Plotting
df.plot(marker='o')

# Adding labels
plt.xlabel("Year")
plt.ylabel("Values")
plt.legend(["Polarity", "Subjectivity"])

# Display the plot
plt.show()    





vvd = dict_programmas_year["VVD"]

# Collect data in a list
sentiment_data = []

for key, text in vvd.items():
    print(key)
    polarity, subjectivity = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer()).sentiment
    sentiment_data.append([key, polarity, subjectivity])


# Create DataFrame outside the loop
df_sentiment = pd.DataFrame(sentiment_data, columns=["year", "polarity", "subjectivity"])
df_sentiment = df_sentiment.sort_values(by="year")


# plot

# Plotting directly from the DataFrame
df_sentiment.plot(x="year", y=["polarity", "subjectivity"], marker='o')

# Adding labels
plt.xlabel("Year")
plt.ylabel("Sentiment Score")
plt.legend(["Polarity", "Subjectivity"])

# Display the plot
plt.show()





    






    

