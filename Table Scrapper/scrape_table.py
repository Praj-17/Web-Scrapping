import schedule
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    url = "https://www.uob.com.sg/online-rates/gold-and-silver-prices.page"
    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get(url)
    soup = BeautifulSoup(browser.page_source)
    nav = browser.find_element_by_id("gld")
    tables = soup.find_all('table')
    df = pd.read_html(str(tables[0]), index_col= None)
    df = pd.DataFrame(df[0], index =None)
    df.to_csv('data.csv', mode='a', header=False)
    print("Data saved sucessfully")

  

if __name__ == '__main__':
    scrape()
    schedule.every(0.5).minutes.do(scrape)
    while True:
        schedule.run_pending()
        time.sleep(1)