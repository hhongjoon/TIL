def diagonal(x,y,loc):
    for i in loc:
        xl , yl = i
        if abs(x-xl) == abs(y-yl):
            return True
    return False


def perm(n,k,loc):
    if n == k:
        global cnt
        cnt+=1
        return
    else:
        for i in range(n):
            if chk[i] == 0:
                if not diagonal(k,i,loc):     # 대각선에 없어야 if문 진행
                    chk[i] = 1
                    temp = loc[:]
                    perm(n,k+1,temp+[(k,i)])
                    chk[i] = 0

N = int(input())
chk = [0]*N
cnt = 0
perm(N,0,[])
print(cnt)

