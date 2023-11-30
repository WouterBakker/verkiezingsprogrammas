# Get pdfs from 2017 & 2021
import requests
import pickle
import sys, os
from collections import defaultdict
from bs4 import BeautifulSoup

class all_verkiezingsprogrammas:
    def __init__(self):
        self.dict_years = defaultdict(list)
        
    def add_verkiezingsprogramma(self, party, year, url, raw_text):
        vp = self.verkiezingsprogramma(party, year, url, raw_text)
        self.dict_years[vp.year].append(vp)

    class verkiezingsprogramma():
        def __init__(self, party, year, url, raw_text):
            self.party = party
            self.year = year
            self.url = url
            self.raw_text = raw_text


urls = ["https://www.parlement.com/id/vk1wljxti6u9/tweede_kamerverkiezingen_2017", 
        "https://www.parlement.com/id/vl4ai9zklwpy/tweede_kamerverkiezingen_2021"]

def parse_urls(url):
    if "rug" in url:
        if "pdf" in url:
            url = os.path.dirname(url)[:-1]
        return url
    
rug_urls = []
    


for url in urls:
    r = requests.get(url)
    s  = BeautifulSoup(r.text, 'html.parser')
    res = s.find_all('a', class_='popup', href = True)
    # rug_urls = [x['href'] for x in res if "rug" in x['href']]
    rug_urls.extend([parse_urls(x['href']) for x in res])

rug_urls = [x for x in rug_urls if x is not None]




def download_pages(urls):
    verkiezingsprogrammas = all_verkiezingsprogrammas()
    
    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            h1_tag = soup.find('h1', class_='ep_tm_pagetitle')
            if h1_tag and 'Item Removed' in h1_tag.get_text():
                print(f'Skipping {url} because it contains "Item Removed"')
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
                        
                        
            page_urls = soup.find_all("a", class_ = "ep_document_link")
            pdf_url = page_urls[0].get("href")
 
            verkiezingsprogrammas.add_verkiezingsprogramma(party, year, pdf_url, soup)

    return verkiezingsprogrammas.dict_years
     
dict_years = download_pages(rug_urls)
programmas = dict_years.copy()

flat_programmas = []

for key in programmas.keys():
    for item in programmas[key]:
        flat_programmas.append(item)
        

sys.setrecursionlimit(10000)

with open('flat_programmas_2017_2021.pkl', 'wb') as file:
    pickle.dump(flat_programmas, file)



def download_pdf(vp):
    """vp = verkiezingsprogramma class"""
    year = vp.year
    party = vp.party
    url = vp.url
    i = 1
    base_str = f"{party}_{year}"
    
    if "/" in base_str:
        base_str = base_str.replace("/", "_")
    
   
    if os.path.exists(f"programmas_pdf/{base_str}.pdf"):
        print("Already downloaded")
        return

    response = requests.get(url)
    print(response.status_code)
    filename = f"programmas_pdf/{base_str}.pdf"
    with open(filename, 'wb') as pdf_file:
        pdf_file.write(response.content)


total_len = len(flat_programmas)

for i, item in enumerate(flat_programmas, 1):
    print(f"Downloading item {i}/{total_len}")
    download_pdf(item)

