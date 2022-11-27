from bs4 import BeautifulSoup
import bs4
import requests
url = 'https://www.engineersedge.com/design_guidelines.htm'
def get_text(url):
    response = requests.get(url)  
    simple_soup = BeautifulSoup(response.text, 'html.parser') 
    paras = simple_soup.find_all('p')
    file_name = url.split('/')[-1]
    
    with open(f'{file_name}.txt', 'w') as f:
        for i in paras:
            f.write(i.text)
    return True