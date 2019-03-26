def bfs(i):
    visited.append(i)
    temp.append(i)
    if len(mat[i]) == 0:
        return 0

    for j in range(len(mat[i])):
        datas[i-1]+=bfs(i)





N, M = map(int,input().split())
mat={}
for i in range(1,N+1):
    mat[i]=[]
# print(mat)
for _ in range(M):
    st, goal = map(int,input().split())
    mat[goal].append(st)
# print(mat)

datas = []

for i in range(1,N+1):

    visited=[]
    temp = []
    bfs(i)
    datas.append(len(visited))
val=max(datas)
print(datas)

for i in range(len(datas)):
    if datas[i] == val:
        print(i+1, end = " ")
print()
