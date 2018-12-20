import requests
from bs4 import BeautifulSoup

req = requests.get("http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum").text
soup = BeautifulSoup(req, 'html.parser')
#aa = soup.select("#asiaBody > table .link") # 국가, 환율
aa = soup.select("#asiaBody > table .link .name") # 국가
bb = soup.select("#asiaBody > table .link .idx") # 환율
country = list()
currency = list()


for i in aa:
    country.append(i.text)

for i in bb:
    currency.append(i.text)

#print(country)
#print(currency)

for ii in range(len(aa)):
    print("{} 의 환율 : {}".format(country[ii], currency[ii]))