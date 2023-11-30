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
    



