import sys
sys.stdin = open('화물도크.txt')
T = int(input())
for _ in range(T):
    N = int(input())
    datas=[]
    for i in range(N):
        datas.append(tuple((map(int,input().split()))))
    datas.sort()
    # print(datas)
    cnt = 1
    piv=0
    temp = datas.pop(0)

    while len(datas)>0:
        loc = datas.pop(0)
        st = loc[0]
        goal = loc[1]
        if st>=temp[0] and goal<=temp[1]:
            temp = loc
            continue
        if loc[0]>=temp[1]:
            temp = loc
            cnt += 1
    print("#{} {}".format(_+1,cnt))