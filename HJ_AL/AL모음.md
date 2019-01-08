### AL모음

```python
#1932 dp
#층계산 함수
def cal_level(loc):
    level = 1
    while loc-level>=0:
        loc = loc - level
        level+=1
    return level

#위치의 최대값 구하기
def cal_max(loc, lev):
    if loc == 0:
        dp[0] = tri[0]
        return 0
        
    if loc - (lev-1)>=0 and loc in x_list1 :
        dp[loc] = dp[loc-(lev-1)] + tri[loc]
        
        
    elif loc - lev >= 0 and loc in x_list2 :
        dp[loc] = dp[loc-lev] + tri[loc]
        #print(loc , dp[loc])
    else:
        dp_r = dp[loc-(lev-1)] + tri[loc]
        dp_l = dp[loc-lev] + tri[loc]
        if dp_r >= dp_l:
            dp[loc] = dp_r
            
        else:
            dp[loc] = dp_l
    #print(loc , dp[loc])
    #print(dp)

def prov1(loc):
    level1 = cal_level(loc)
    count = 0
    x_list=[]
    for i in range(level1):
        count += i
        x_list.append(count)
    return x_list
        
def prov2(loc):
    level1 = cal_level(loc)
    count = 0
    x_list=[]
    for i in range(2, level1+2):
        
        x_list.append(count)
        count += i
    return x_list
        
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
#입력부
count = int(input())
tri = []
for i in range(count):
    aa = list(map(int, input().split()))
    tri = tri+aa




#dp 초기화
dp = []
for i in range(len(tri)):
    dp.append(0)

x_list1 = prov1(len(tri)-1)
x_list2 = prov2(len(tri)-1)

#print(tri)
# 구하기

for i in range(len(tri)):
    i_level = cal_level(i)
    cal_max(i,i_level)
    

print(max(dp))

#print(dp)
#print(i_max)
```

```python
#11066 dp


```

