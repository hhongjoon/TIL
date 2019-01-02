from bs4 import BeautifulSoup
import requests
import random


numbers = random.sample(range(800,838),8)
print (numbers)

for i in numbers:
    #requests
    # for j in aa:
    #     print(j.text, end = ' ')
    # print()
    url =  "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(i)
    #url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={i}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    aa = soup.select("#article .ball_645")
    print("{} 회차입니다.".format(i))
    #print(f"{i} 회차 당첨번호")
    

    for j in range(len(aa)-1):
        print(aa[j].text, end = ' ')
    print('+ ' + aa[-1].text, end = ' ')
    
    print()
#BeautifulSoup
#fromlect
#pirnt 몇회차 당첨번호

