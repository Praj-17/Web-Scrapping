import requests
from bs4 import BeautifulSoup
import pandas as pd

sheet_url = "https://docs.google.com/spreadsheets/d/1fBx_dmkWVias5UVBIJw_zGdh46GcHcEB/edit#gid=959784854"
url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

input_file = pd.read_csv(url)
print(type(input_file))

for URL_ID, URL  in enumerate(input_file['URL']):
    print(URL)
    print(URL_ID+1)
    with open(f'{int(URL_ID)+1}.txt', 'x+') as f:
        content = requests.get(URL)
        htmlcontent = content.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        # f.write(title.string)
        paras = soup.find_all('p')
        for para in paras:
           string =  para.get_text()
           f.write(string)
## Browser giving Problem Having Trouble will fix it soon.
