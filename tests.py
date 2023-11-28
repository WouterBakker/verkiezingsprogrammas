import requests
from bs4 import BeautifulSoup



url = 'https://www.parlement.com/id/vh8lnhrp8wsx/tweede_kamerverkiezingen_2002'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

hyperlinks = soup.find_all('a')

ptags = soup.find_all('p')

ptags[112]

ptags[112].get('href')

"dnpprepo" in ptags[112]




atags = soup.find_all('a')


for atag in atags:
    atag.get('href')
    
    
'dnpprepo' in 'http://dnpprepo.ub.rug.nl/433/'



links = []
for atag in atags:
    res = atag.get('href')

    if res and 'dnpprepo' in res:
        links.append(res)
        
        
        
url = "https://dnpprepo.ub.rug.nl/300/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


a = soup.find_all('th')

for x in a:
    print(x.get_text())
    
    
for x in a:
    if x.get_text() == "Date of elections:":
        sib = x.find_next_sibling()
        print(sib.get_text().split(" ")[-1])



for x in a:
    if x.get_text() == "Purpose:":
        print(x.find_next_sibling().get_text())
        b = x.find_next_sibling().get_text()


c = soup.find_all("a", class_ = "ep_document_link")

c[0].get("href")