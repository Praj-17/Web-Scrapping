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
from typing import *

def countPairs(a: List[int], n: int, k: int) -> int:
	T = int(input())
    for i in range(T):
        count =0
        N, k = list(map(input().split(), int))
        array = list(map(input().split(), int))
        for i in array:
            for j in array:
                if sum(i,j)/2 >= k: count = count+1
        (count)