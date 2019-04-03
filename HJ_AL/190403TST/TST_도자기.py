
def comb(n,k,c):
    global M
    if c == M:
        temp=[]
        for i in range(len(A)):
            if A[i] == 1:
                temp.append(datas[i])
        # print(temp)

        res.add(tuple(temp))

    if n == k:
        return
    else:
        A[k]=1
        comb(n,k+1,c+1)
        A[k]=0
        comb(n,k+1,c)


T = int(input())
for _ in range(1,T+1):
    N, M = map(int,input().split())
    datas = list(map(int,input().split()))
    datas.sort()
    A=[0]*len(datas)
    res = set()
    comb(N,0,0)
    print(len(res))