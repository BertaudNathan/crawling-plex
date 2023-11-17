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
options.headless = True

browser = webdriver.Chrome(options=options)

browser.get('https://thepiratebay.org/index.html')

search_bar = browser.find_element(By.CSS_SELECTOR, "input")
arguments = sys.argv[1:]
search_bar.send_keys(arguments)
search_bar.send_keys(Keys.ENTER)

wait = WebDriverWait(browser, 7)


time.sleep(1)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

links = browser.find_elements(By.CSS_SELECTOR, 'a')

count = 0

for link in links:
    href = link.get_attribute('href')
    if 'https://thepiratebay.org/description.php?id=' in href:
        mongarss = href
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
        boubou = a['href']
        break

browser.quit()