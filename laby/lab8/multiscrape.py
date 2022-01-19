import requests
import os
from PIL import Image
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor

def improc(name):
    print(name + " na procesie nr {}".format(os.getpid()))
    src = "http://if.pw.edu.pl/~mrow/dyd/wdprir/" + name
    img_data = requests.get(src).content
    with open(name, 'wb') as handler:
        handler.write(img_data)
    img = Image.open(name)
    imgGray = img.convert('L')
    imgGray.save(name)
    print(name + " skonwertowany")

if __name__=='__main__':
    req = requests.get('http://if.pw.edu.pl/~mrow/dyd/wdprir/')
    soup = BeautifulSoup(req.text, 'html.parser')
    alist = soup.find_all('a')
    pool = ProcessPoolExecutor(max_workers=12)
    tasks = []
    for item in alist:
        if ".png" in item.get_text():
            tasks.append(pool.submit(improc,(item.get_text())))