def cal(tt):
    summ =0
    for i in range(len(homes)):
        minsum = 9999999
        for j in range(len(tt)):
            t = abs(homes[i][0] - tt[j][0]) + abs(homes[i][1] - tt[j][1])
            if minsum > t:
                minsum = t
        summ += minsum

    return summ

def caldis():
    temp = []
    for i in range(len(A)):
        if A[i] == 1:
            temp.append(chikens[i])

    global mindis
    res = cal(temp)
    if mindis > res:
        mindis = res

def comb(n,k,c):

    if c == M:
        # print(A)
        caldis()
        return
    if n == k:
        return
    else:
        A[k] = 1
        comb(n, k+1, c+1)
        A[k] = 0
        comb(n,k+1,c)


N, M = map(int,input().split())
homes = []
chikens = []
mat = [ list(map(int,input().split())) for i in range(N) ]
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            homes.append((i,j))
        if mat[i][j] == 2:
            chikens.append((i,j))
# print(chikens,'c')
# print(homes,'h')
mindis = 0xffffff
A = [0]*len(chikens)
comb(len(chikens),0,0)
print(mindis)

