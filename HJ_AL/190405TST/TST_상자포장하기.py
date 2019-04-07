
def comb(n,k,a,b,ac,bc):
    global maxsum

    if n == k:
        maxsum = max(maxsum,ac+bc)
        return
    else:
        if datas[k]<a:
            comb(n,k+1,datas[k],b,ac+datas[k],bc)
        if datas[k]>b:
            comb(n, k + 1, a, datas[k], ac , bc + datas[k])
        comb(n,k+1,a,b,ac,bc)

T = int(input())
for _ in range(T):
    N = int(input())
    datas = list(map(int,input().split()))
    maxsum = -1
    comb(N,0,1001,0,0,0)
    print(maxsum)