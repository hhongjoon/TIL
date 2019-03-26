import sys
sys.stdin = open('컨테이너 운반.txt')

def move(W,T_W):
    dis = 0
    while len(T_W)>0 and len(W)>0:
        j =0
        tr = T_W.pop()
        while j<len(W):
            if tr - W[j]<0:
                if j == 0:
                    break
                dis += W.pop(j-1)
                break

            if j == len(W)-1:
                dis+=W.pop()
                break
            j+=1

    return dis

T = int(input())
for _ in range(T):
    C, T = map(int,input().split())
    w = list(map(int,input().split()))
    w.sort()
    t_w = list(map(int,input().split()))
    t_w.sort()

    maxload = move(w,t_w)
    print("#{} {}".format(_+1,maxload))