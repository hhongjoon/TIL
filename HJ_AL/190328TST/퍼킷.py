

def powerset(n,k,s,b):
    global minmat
    if minmat ==0:
        return

    if b!=0:
        if minmat > abs(s-b):
            minmat = abs(s-b)
    if n ==k:
        return
    else:
        A[k] = 1
        plus = datas[k]
        powerset(n,k+1,s*plus[0], b+plus[1])
        A[k] = 0
        powerset(n,k+1,s,b)



N = int(input())
datas=[]
A = [0]*N
for i in range(N):
    datas.append(tuple(map(int,input().split())))

minmat = 0xffffff
powerset(N,0,1,0)
print(minmat)