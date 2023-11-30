import os

txts = os.listdir("programmas_txt")

data = {}

a = []

for txt in txts:
    key = os.path.splitext(txt)[0].split("_")
    a.append(txt)
    
    

# Open the file in read mode ('r')
for txt in txts:
    key = os.path.splitext(txt)[0].split("_")
    
    file_path = f"programmas_txt/{txt}"
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the entire content of the file
        output = file.read().replace('\n', ' ')
    
    
        
        
a = os.path.basename(f"programmas_txt/{txts[0]}")

b = os.path.splitext(txts[0])[0].split("_")

b

    