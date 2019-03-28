def cal(n,k,cnt):
    global flag
    if flag == True:
        return

    if cnt == K:
        flag = True
        return
    if n ==k :
        return
    else:
        chk[k] = 1
        cal(n,k+1,cnt+datas[k])
        chk[k] = 0
        cal(n,k+1,cnt)


T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    datas = list(map(int,input().split()))
    chk=[0]*N
    flag = False
    cal(N,0,0)
    if flag:
        print('YES')
    else:
        print('NO')