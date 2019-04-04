
def findloc(n):

    for i in range(N):
        for j in range(0,i+1):
            if mat[i][j] == 1 and i==n :
                path[j]=1
            if mat[i][j] == 1 and j==n :
                path[i]=1



N, M = map(int,input().split())
mat = [ list(map(int,input().split())) for i in range(N) ]
# print(mat)

visited = [-1]*N
for i in range(N):
    flag = False
    colors = [False] * M
    path = [0] * N
    findloc(i)
    for j in range(len(path)):
        if path[j] == 1:
            if visited[j] == -1:
                continue
            colors[visited[j]]=True
    for j in range(len(colors)):
        if colors[j] == True:
            continue
        flag=True
        visited[i] = j
        break

if flag == False:
    print(-1)
else:
    for i in visited:
        print(i+1, end=" ")

