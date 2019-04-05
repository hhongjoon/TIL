
def comb(n,k,floor):  # n: 기준 k:현재길이/ 층
    global flag, maxfloor
    if not flag:
        return

    if n == k:
        # print('@@@@@@@@@')
        maxfloor = max(maxfloor,floor)
        return
    else:
        for i in range(k+1,N+1):
            temp = datas[k:i]
            if len(temp) ==0: continue
            if len(temp)== 1 and i != N:
                if temp[0] != 2: continue

            if len(temp) == 2 and (temp.count(1) == 2 or temp.count(3) == 2) :
                if i != N:
                    flag = False
            # print(temp)
            comb(n,i,floor+1)

T = int(input())
for _ in range(T):
    N = int(input())
    datas = list(map(int,input().split()))
    A = [0]*len(datas)
    flag = True
    maxfloor = -1
    comb(N,0,0)
    if flag:
        print(maxfloor)
    else:
        print(-1)