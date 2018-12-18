import requests
from bs4 import BeautifulSoup

req = requests.get("https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1h").text
soup = BeautifulSoup(req, 'html.parser')
aa = soup.select("tbody .name ")

for i in aa:
    print(i.text)


