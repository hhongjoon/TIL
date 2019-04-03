
def cal():
    summ = 0
    for i in range(len(coms)):
        if coms[i] == 0:
            continue
        summ += mat[coms[i]-1][i+1]
    return summ
def perm(n,k,c):
    if n-1 == k:
        coms[n-1] = M-c
        res = cal()
        global maxdis
        if maxdis<res:
            maxdis = res
        # print(coms)
        return
    else:
        for i in range(0,M-c+1):
            coms[k] = i
            perm(n,k+1,c+i)



M , N = map(int,input().split())
mat = [ list(map(int,input().split())) for i in range(M) ]

maxdis = -1
coms = [0]*N
perm(N,0,0)
print(maxdis)