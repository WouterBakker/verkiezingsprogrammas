import os
import pandas as pd
import spacy
import pickle
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

    
with open('dict_programmas_all.pkl', 'wb') as file:
    pickle.dump(dict_programmas_all, file)

with open('dict_programmas_year.pkl', 'wb') as file:
    pickle.dump(dict_programmas_year, file)




    






    

