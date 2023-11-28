import requests
import pickle
import sys, os


class Verkiezingsprogramma:
    def __init__(self, party, year, url, raw_text):
        self.party = party
        self.year = year
        self.url = url
        self.raw_text = raw_text
        

def download_pdf(vp):
    """vp = verkiezingsprogramma class"""
    year = vp.year
    party = vp.party
    url = vp.url
    i = 1
    base_str = f"{party}_{year}"
    # while os.path.exists(f"programmas/{base_str}.pdf"):
    #     base_str += f"_{i}"
        
    if os.path.exists(f"programmas/{base_str}.pdf"):
        return

    response = requests.get(url)
    print(response.status_code)
    filename = f"programmas/{base_str}.pdf"
    with open(filename, 'wb') as pdf_file:
        pdf_file.write(response.content)

# sys.setrecursionlimit(10000)

with open('flat_programmas.pkl', 'rb') as file:
    programmas = pickle.load(file)

total_len = len(programmas)

for i, item in enumerate(programmas, 1):
    print(f"Downloading item {i}/{total_len}")
    download_pdf(item)

