
def perm(n,k,a,b, preva, prevb):
    if n == k:
        global maxsum
        if maxsum < a+b:
            maxsum = a+b
        return
    else:
        plus = datas[k]


        if preva is None or preva>plus:
            perm(n,k+1,a+plus,b,plus,prevb)
        if prevb is None or prevb < plus:
            perm(n, k+1, a, b+plus,preva,plus)

        perm(n, k+1, a, b,preva,prevb)


T = int(input())
for _ in range(T):
    N = int(input())
    datas = list(map(int,input().split()))
    chk = [0]*N
    maxsum = -1
    perm(N,0,0,0,None,None)
    print(maxsum)