import requests
from bs4 import BeautifulSoup

#print(requests.get("http://www.naver.com").text) 
#print(requests.get("http://www.naver.com").status_code)
req = requests.get("https://www.naver.com/").text

soup = BeautifulSoup(req, 'html.parser')

kospi=soup.select(".ah_a .ah_k")
#print(kospi)


#kk = list()
for i in kospi:
    #kk.append(list(i))
    print(i.text)
    

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

url = "www.naver.com"   # 강사님 코드
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')
for tag in soup.select():
    rank = tag.select_one('.ah_r').text
    name = tag.select_one('.ah_k').text
    print(f'{rank}는 {name} 입니다.')
