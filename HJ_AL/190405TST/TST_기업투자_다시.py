
def comb(n,k,c):  # 전체돈,회사,금액
    if c == M and k==N:
        # 계산
        print(coms)
        return
    if k == N:
        return
    else:
        for i in range(0,n+1):
            coms[k] = i
            comb(n,k+1,c+i)


M, N = map(int,input().split())
mat = [ list(map(int,input().split()))  for i in range(N+1) ]
coms = [0]*N
comb(M,0,0)