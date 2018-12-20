import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.op.gg/summoner/userName=킹싸피").text
soup = BeautifulSoup(req, 'html.parser')
#aa = soup.select("#marketindexLastList .stock_dn .item_wrp .stock_item")
aa = soup.select_one(".SummonerRatingMedium .tierRank")



print(aa.text)

