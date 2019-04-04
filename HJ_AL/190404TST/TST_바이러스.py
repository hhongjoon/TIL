
def bfs(n):
    Q=[]
    Q.append(n)
    visited[n]=True
    while len(Q):
        temp = Q.pop(0)
        for i in range(N):
            if mat[temp][i] == 1:
                if visited[i] == False:
                    visited[i]= True
                    Q.append(i)

N = int(input())
M = int(input())
mat = [ [0]*N for i in range(N) ]
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    mat[a][b] = mat[b][a] =1

visited = [False]*N
bfs(0)
print(visited.count(True)-1)

