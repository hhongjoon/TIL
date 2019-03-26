def cal(n,summ):
    temp = summ
    temp += len(mat[n])
    for i in mat[n]:
        temp += cal(i,0)
    bigmat[n-1] = temp
    print(bigmat)
    return temp

N, M = map(int,input().split())
mat={}
for i in range(1,N+1):
    mat[i]=[]
# print(mat)
for _ in range(M):
    st, goal = map(int,input().split())
    mat[goal].append(st)
# print(mat)
bigmat=[None]*N
datas=[]
for i in range(1,N+1):
    datas.append(cal(i,1))
print(bigmat)
val = max(datas)
for j in range(len(datas)):
    if datas[j] == val:
        print(j+1,end=" ")
