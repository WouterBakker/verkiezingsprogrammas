import spacy
import os


nlp = spacy.load('nl_core_news_sm')
txts = os.listdir("programmas_txt")

# Specify the path to your text file
file_path = f"programmas_txt/{txts[1]}"

# Open the file in read mode ('r')
with open(file_path, 'r', encoding='utf-8') as file:
    # Read the entire content of the file
    data = file.read().replace('\n', ' ')
    
    
# Open the file in read mode ('r')
with open("programmas_txt/VVD_2012.txt", 'r', encoding='utf-8') as file:
    # Read the entire content of the file
    data = file.read().replace('\n', ' ')
    
    
    
# Process the text with spaCy
doc = nlp(data)

# Extract entities
entities = [(ent.text, ent.label_) for ent in doc.ents]



# Print the entities
print(entities)
    


## Categorize the words with spacy
# Process the text with spaCy

# pvv_counts = dict_wordcounts['PVV']
# pvv_text = dict_programmas_all["PVV"]

# doc = nlp.pipe(pvv_text)

# words_pos = {x.text: x.pos_ for x in doc}

# for key, item in words_pos.items():
#     print(f"{key}: {item}")
    
    



