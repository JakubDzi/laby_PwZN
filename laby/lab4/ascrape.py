from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import json
import argparse

parser = argparse.ArgumentParser(description="Program zbiera dane ze strony internetowej")
parser.add_argument('file', help='nazwa pliku z wynikami')
args = parser.parse_args()

options=Options()
options.add_argument('--disable-notifications')
service=Service('./chromedriver.exe')
driver=webdriver.Chrome(service=service, options=options)
driver.get('https://www.python.org')
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("numpy")
search_bar.send_keys(Keys.RETURN)
req = requests.get(driver.current_url)
soup = BeautifulSoup(req.text, 'html.parser')
divs_artlist = soup.find('ul', class_ = 'list-recent-events menu')
divs_arttit = divs_artlist.find_all('h3')
chartt=[]
for div in divs_arttit:
    chartt.append(div.find('a').text.strip())
with open (args.file+'.json', 'w') as f:
    json.dump(chartt, f)