
#Import libraries
import os
import wget

from matplotlib import widgets
from GoogleImageScrapper import GoogleImageScraper
from patch import webdriver_executable

if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys= ['modi', 'elon musk', 'bill gates', 'ms dhoni', 'virat kohli', 'arnab goswami', 'nambi narayan', 'abdul kalam', 'rakesh jhunjhunwala', 'warren buffet', 'charlie munger', 'justin bieber', 'jeff bezos', 'goutam adani', 'mukesh ambani', 'ratan tata', 'kapil sharma', 'daya bhabhi', 'jethalal', 'bhide bhai', 'babitaji', 'mahatma gandhi', 'madhvi bhabhi', 'bagha', 'nattu kaka', 'bavari', 'taarak mehta real', 'shailesh lodha', 'iyyer bhai', 'popatlal', 'tipendra gada', 'alia bhat']

    #Parameters
    number_of_images = 2
    headless = False
    min_resolution=(0,0)
    max_resolution=(9999,9999)

    #Main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
        image_urls = image_scrapper.find_image_urls()
        wget.download(image_urls)
        image_scrapper.save_images(image_urls)
        print("Image saved")
    
    #Release resources    
    del image_scrapper