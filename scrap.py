import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time

options = Options()
options.add_argument("--headless=new")

browser = webdriver.Chrome(options=options)
Movies = sys.argv[1]
browser.get('https://thepiratebay.org/search.php?q=' + Movies + '&cat=207')

search_bar = browser.find_element(By.CSS_SELECTOR, "input")

time.sleep(1)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

links = browser.find_elements(By.CSS_SELECTOR, 'a')
size = soup.find('span', class_="list-item item-size")
print(size.text)
    
count = 0

for link in links:
    href = link.get_attribute('href')
    if 'https://thepiratebay.org/description.php?id=' in href:
        mongarss = href
        print(href)
        count = count + 1
        if count == 2 and size.text.__contains__("GiB"):
            value = size.text.__contains__("GiB")
            gh = value[:len(value)-4]
            gh = int(gh)
            if gh > 4:
                print("trop lourd mon pote")
                break
            else:
                continue
        else :
            break
browser.quit()

browser = webdriver.Chrome(options=options)
browser.get(mongarss)

time.sleep(2)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
for a in soup.find_all('a', href=True):
    if "magnet" in a['href']:
        print (a['href'])
        break
    

browser.quit()