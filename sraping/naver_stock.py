import requests
from bs4 import BeautifulSoup

req = requests.get("https://m.stock.naver.com/marketindex/index.nhn").text
soup = BeautifulSoup(req, 'html.parser')
aa = soup.select("#marketindexLastList .stock_dn .item_wrp .stock_item")

for i in aa:
    print(i.text)