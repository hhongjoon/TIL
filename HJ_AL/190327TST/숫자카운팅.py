def calsame(loc,datas,n):  # loc은 현재위치(중간값위치,리스트,찾으려는 숫자
    org = datas[:]
    cnt = 1
    i=loc
    datas = org[loc+1:]
    while True:  # 오른쪽
        if len(datas) ==0:
            break
        loc = len(datas)//2
        if datas[loc]>n:
            datas=datas[:loc]
        else:
            datas = datas[loc:]
            cnt +=loc

    loc = i
    datas = org[:loc]
    while True:  # 왼쪽
        if len(datas) ==0:
            break
        loc = len(datas)//2
        if datas[loc]<n:
            datas=datas[loc+1:]
        else:
            cnt += (len(datas) - loc)
            datas = datas[:loc]


    return cnt

    # while True and i <len(datas):
    #     if datas[i] != n:
    #         break
    #     cnt+=1
    #     i+=1
    # i = loc -1
    # while True and i>-1:
    #     if datas[i] != n:
    #         break
    #     cnt+=1
    #     i-=1
    #
    # return cnt


def findB(n,datas):
    while True:
        if len(datas) == 0:
            return 0
        else:

            loc = len(datas)//2
            if datas[loc]<n:
                datas = datas[loc+1:]
            elif datas[loc] == n:
                return calsame(loc,datas,n)
            else:
                datas = datas[:loc]


    pass


N = int(input())
datas = list(map(int,input().split()))
M = int(input())
M_dat = list(map(int,input().split()))
for i in M_dat:
    print(findB(i,datas), end=" ")

