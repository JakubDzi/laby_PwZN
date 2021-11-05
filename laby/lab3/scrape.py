import argparse
from rich.console import Console
import rich.traceback
import requests
import json
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Program zbiera dane ze strony internetowej")
parser.add_argument('file', help='nazwa pliku z wynikami')
args = parser.parse_args()

console = Console()
console.clear()
rich.traceback.install()

req = requests.get('https://www.imdb.com/title/tt0076759/fullcredits/?ref_=tt_cl_sm')
soup = BeautifulSoup(req.text, 'html.parser')
divs_cast_list = soup.find('table', class_ = 'cast_list')
divs_charso = divs_cast_list.find_all('tr', class_='odd')
divs_charse = divs_cast_list.find_all('tr', class_='even')
liczba=len(divs_charso)+len(divs_charse)
chartt=[]
for i in range(liczba):
    chartt.append([])
iter=0
with open (args.file+'.json', 'w') as f:
    for dc in divs_charso:
        chartt[iter].append(dc.find('img')['title'])
        chartt[iter].append(dc.find('td', class_='character').find('a').text.strip())
        iter = iter + 1
    for dc in divs_charse:
        chartt[iter].append(dc.find('img')['title'])
        chartt[iter].append(dc.find('td', class_='character').find('a').text.strip())
        iter = iter + 1
    json.dump(chartt, f)