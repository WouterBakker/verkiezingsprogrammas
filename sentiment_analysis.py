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




