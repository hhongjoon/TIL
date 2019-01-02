import requests
from bs4 import BeautifulSoup

req = requests.get("https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=836").text
soup = BeautifulSoup(req, 'html.parser')
#aa = soup.select("#marketindexLastList .stock_dn .item_wrp .stock_item")
aa = soup.select("#article .num.win .ball_645")


for i in aa:
    print(i.text)