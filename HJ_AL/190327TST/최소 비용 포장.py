

def perm(n,k,dis):
    global mindis
    if dis>=mindis:
        return
    if n == k:
        if mindis>dis:
            mindis = dis
        # print(dis)
        return
    else:
        for i in range(k,len(datas)):
            datas[i], datas[k] = datas[k], datas[i]


            if k<=1:
                perm(n,k+1,dis+datas[k])
            else:
                perm(n,k+1,dis+dis+datas[k])
            datas[i], datas[k] = datas[k], datas[i]

    pass
N = int(input())
datas = list(map(int,input().split()))
mindis = 9999999999

# Nf = 1
# for i in range(1,N+1):
#     Nf*=i
#
# datasT=[ [0]*Nf for i in range(N) ]
# print(Nf)




perm(N,0,0)
print(mindis)
