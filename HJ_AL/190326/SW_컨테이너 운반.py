import sys
sys.stdin = open('컨테이너 운반.txt')

def move(T,dis,W,T_W):



    global maxload
    if len(T_W) == 0 or len(W) == 0:
        if maxload<dis:
            maxload = dis
        # print(dis)
        return
    else:
        if min(W) > T_W[-1]:
            tempW = W[:]
            tempT = T_W[:]
            tempT.pop()
            move(T, dis, tempW, tempT)

        for i in range(len(W)):
            if T_W[-1] < W[i]: continue
            tempW = W[:]
            plus = tempW.pop(i)
            tempT = T_W[:]
            tempT.pop()
            move(T,dis+plus,tempW,tempT)


T = int(input())
for _ in range(T):
    C, T = map(int,input().split())
    w = list(map(int,input().split()))
    w.sort()
    t_w = list(map(int,input().split()))
    t_w.sort(reverse=True)
    maxload = 0
    move(T,0,w,t_w)
    print("#{} {}".format(_+1,maxload))


