import random
import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint

# 랜덤으로 로또번호 생성 (우리꺼)
# API 통해 우승 번호 가져옴
# 두개를 비교해 나의 등수를 알려줌
# -------
# url요청보내서 정보 가져옴
#    - json으로 받는다
# api 당첨번호와 보너스 번호 저장
# 뽑은게 몇등인지 뽑을 것 

my_nums = random.sample(range(1,46),6)
my_nums=set(my_nums)
print(my_nums)
#print(type(my_nums))
# 우승번호
url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json() # json으로 받아옴

#pprint(lotto)
lotto['drwtNo1']
win_nums = set()
for i in range(1,7):
    win_num = lotto[f'drwtNo{i}']
    win_nums.add(win_num)
bonus = lotto['bnusNo']
print(win_nums)

count = 1
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
while count <50000000 : # 들여쓰기 블록 + tab
    if len(win_nums & my_nums) == 6:
        print('1등입니다.')
        a1+=1
        break
        
    if len(win_nums & my_nums) == 5:
        if bonus in my_nums:
            print('2등입니다.')
            a2+=1
        else :
            print('3등입니다.')
            a3+=1
    if len(win_nums & my_nums) == 4:
        print('4등입니다.')
        a4+=1
    if len(win_nums & my_nums) == 3:
        print('5등입니다.')   # money = format(count*1000, ',') 하면 원화로 표시됨
        a5+=1
    else:
        print(count)

    count += 1
    my_nums = random.sample(range(1,46),6)
    my_nums=set(my_nums)


print(f'1위 : {a1}')
print(f'2위 : {a2}')
print(f'3위 : {a3}')
print(f'4위 : {a4}')
print(f'5위 : {a5}')



# print(type(res))
# print(res)
# pprint.print(res)

# my_nums = random.sample((1,46),6)
# # set 이용
# win_nums= list()

# req = requests.get().text
# soup = BeautifulSoup(req,'html.parse')
# aa = soup.