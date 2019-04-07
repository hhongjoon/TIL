
def powerset(n,k,cnt,c):
    global mindis
    if c== n//2:
        if mindis > abs((summ - cnt) - cnt):
            mindis = abs((summ - cnt) - cnt)
        return

    if n==k:
        return
    else:
        plus = datas[k]
        powerset(n,k+1,cnt+plus,c+1)

        powerset(n,k+1,cnt,c)

N = int(input())
datas = list(map(int,input().split()))
summ = sum(datas)
mindis = 999999
powerset(N,0,0,0)
print(mindis)