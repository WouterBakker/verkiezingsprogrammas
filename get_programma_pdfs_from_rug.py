import requests
import pickle

def download_pdf(vp):
    """vp = verkiezingsprogramma class"""
    year = vp.year
    party = vp.party
    url = vp.url
    i = 1
    base_str = f"{party}_{year}"
    while os.path.exists(f"{base_str}.pdf"):
        base_str += f"_{i}"

    response = requests.get(url)
    print(response.status_code)
    filename = f"{base_str}.pdf"
    with open(filename, 'wb') as pdf_file:
        pdf_file.write(response.content)

with open('flat_programmas.pkl', 'rb') as file:
    programmas = pickle.load(file)


for item in subs:
    download_pdf(item)

