import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/"
req = requests.get(url).text

soup = BeautifulSoup(req,'html.parser')
kospi = soup.select_one('#KOSPI_now').text
print(kospi)

# print(req)
# print(req.text)
# print(req.status_code)

