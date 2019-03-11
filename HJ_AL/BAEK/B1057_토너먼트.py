# 1-N,
N, kim, lim = map(int,input().split())
roundcnt = 1
while True:
    if kim == lim:
        print(roundcnt - 1)
        break
    kim = (kim+1)//2
    lim = (lim+1)//2
    roundcnt +=1
