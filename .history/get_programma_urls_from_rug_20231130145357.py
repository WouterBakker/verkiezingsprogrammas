import requests
from bs4 import BeautifulSoup
import os, sys
import pickle


class Verkiezingsprogramma:
    def __init__(self, party, year, url, raw_text):
        self.party = party
        self.year = year
        self.url = url
        self.raw_text = raw_text
        
        
class dict_Verkiezingsprogramma:
    def __init__(self):
        self.dict_years = {}
    
    def add_verkiezingsprogramma(self, Verkiezingsprogramma):
        if Verkiezingsprogramma.year in self.dict_years:
            self.dict_years[Verkiezingsprogramma.year].append(Verkiezingsprogramma)
        else:
           self.dict_years[Verkiezingsprogramma.year] = [Verkiezingsprogramma] 

def download_pages(id):

    verkiezingsprogrammas = dict_Verkiezingsprogramma()
    
    counter = 0
    for i in range(1, id):
        url_rug = f"https://dnpprepo.ub.rug.nl/{i}"     
        response = requests.get(url_rug)
        print(i)
        print(response)
        print(url_rug)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            h1_tag = soup.find('h1', class_='ep_tm_pagetitle')
            if h1_tag and 'Item Removed' in h1_tag.get_text():
                print(f'Skipping {url_rug} because it contains "Item Removed"')
                continue
            
            th_tags = soup.find_all('th')
            for tag in th_tags:
                text = tag.get_text()
                                    
                if text == "Party:":
                    party = tag.find_next_sibling().get_text()
                if text == "Purpose:":
                    purpose = tag.find_next_sibling().get_text()
                if text == "Date of elections:":
                    date = tag.find_next_sibling().get_text()
                    try:
                        year = int(date.split(" ")[-1])
                    except:
                        year = date


            if purpose != "Tweede Kamerverkiezingen":
                counter += 1
                continue
            
            urls = soup.find_all("a", class_ = "ep_document_link")
            url = urls[0].get("href")
            
            res = Verkiezingsprogramma(party, year, url, soup)
            verkiezingsprogrammas.add_verkiezingsprogramma(res)
                   
                        
        if counter > 100:
            print(f"Finished at iteration: {i}")
            break

    return verkiezingsprogrammas.dict_years
        
            
programmas = download_pages(1000)

sorted_keys = sorted(programmas, reverse = True)
sorted_programmas = {x: programmas[x] for x in sorted_keys}

flat_programmas = []

for key in programmas.keys():
    for item in programmas[key]:
        flat_programmas.append(item)


sys.setrecursionlimit(10000)

with open('flat_programmas.pkl', 'wb') as file:
    pickle.dump(flat_programmas, file)



