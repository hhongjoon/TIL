

def powerset(n,k,cnt):  # 부분집합 구하는 것처럼 2^n
    global minch

    if minch == 0:
        return

    if cnt>=B:
        if minch>cnt-B:
            minch = cnt-B
        return
    if n == k:
        return
    else:
        A[k]=1
        powerset(n,k+1,cnt+datas[k])
        A[k]=0
        powerset(n,k+1,cnt)

T = int(input())
for _ in range(T):
    N, B = map(int,input().split())
    datas=[]
    A=[0]*N
    for i in range(N):
        datas.append(int(input()))

    minch = 0xffffff
    powerset(N,0,0)
    print(minch)