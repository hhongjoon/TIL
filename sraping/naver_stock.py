import requests
from bs4 import BeautifulSoup

req = requests.get("https://m.stock.naver.com/marketindex/index.nhn").text
soup = BeautifulSoup(req, 'html.parser')
#aa = soup.select("#marketindexLastList .stock_dn .item_wrp .stock_item")
aa = soup.select("#marketindexLastList .item_wrp .stock_item")
bb = soup.select("#marketindexLastList .price_wrp .stock_price")

for i in aa:
    print(i.text)

for a in bb:
    print(a.text)

for i in range(len(aa)):
    print("{}     {}".format(aa[i].text, bb[i].text))