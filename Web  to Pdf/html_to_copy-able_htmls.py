from bs4 import BeautifulSoup
import bs4
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
url = 'https://www.engineersedge.com/design_guidelines.htm'

def get_text(url):

    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get(url)
    simple_soup = BeautifulSoup(browser.page_source)

    file_name = url.split('/')[-1]
    
    with open(f'Htmls//{file_name}.html', 'w') as f:
        f.write('simple_soup')
    print(f'Done with {file_name}')
    return True