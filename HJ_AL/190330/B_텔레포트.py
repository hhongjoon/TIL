import sys
sys.setrecursionlimit(2000)

def cal_dis(k1, k2):

    if k1[0]==1 and k2[0]==1:
        plus = min(T,abs(k1[1]-k2[1])+abs(k1[2]-k2[2]))
    else:
        plus = abs(k1[1]-k2[1])+abs(k1[2]-k2[2])
    return plus


def powerset(s,e,n,k,cnt):
    global mindis
    # print(s, k, cnt)
    if s == e:
        if mindis > cnt:
            mindis = cnt
        return
    if cnt>=mindis:
        return
    if n+1==k:
        return
    else:
        # A[k] = 1
        plus = cal_dis(s,datas[k])
        powerset(datas[k],e,n,k+1,cnt+plus)
        # A[k] = 0
        powerset(s,e,n,k+1,cnt)




N, T = map(int,input().split())
datas = [0]*(N+1)

for i in range(1,N+1):
    s,x,y = map(int,input().split())
    datas[i] = (s,x,y)
# print(datas)
M = int(input())
for _ in range(M):
    s1,e1 = map(int,input().split())
    if s1 > e1:
        s1,e1 = e1,s1
    s = datas[s1]
    e = datas[e1]
    if s[0]==1 and e[0]==1:
        mindis = min(T,abs(s[1]-e[1])+abs(s[2]-e[2]))
    else:
        mindis = abs(s[1]-e[1])+abs(s[2]-e[2])

    # A = [0]*(N+1)
    powerset(s,e,N,1,0)
    print(mindis)



