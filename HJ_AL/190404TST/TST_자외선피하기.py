def iswall(x,y):
    if x>-1 and y>-1 and x<N and y< N:
        return False
    return True

def bfs(x,y):
    global gx, gy
    Q = []
    visited[x][y] = mat[x][y]
    Q.append((x,y))
    while len(Q)>0:
        x, y = Q.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if iswall(nx,ny): continue
            if visited[nx][ny] > visited[x][y] + mat[nx][ny]:
                visited[nx][ny] = visited[x][y] + mat[nx][ny]
                Q.append((nx,ny))



N = int(input())
mat = [ list(map(int,input())) for i in range(N) ]

visited = [ [9999]*N for i in range(N) ]
dx =[0, 1, 0, -1 ]
dy =[1, 0, -1, 0]

bfs(0,0)
print(visited[N-1][N-1])