

def iswall(x,y):
    if x>-1 and y>-1 and x<X and y<Y:
        return False
    return True

def bfs(sx,sy,ex,ey):
    visited[sx][sy]=1
    Q=[]
    Q.append((sx,sy))
    while len(Q)>0:
        temp = Q.pop(0)
        x = temp[0]
        y = temp[1]

        if x==ex and y==ey:
            return visited[x][y] -1


        for i in range(8):
            nx = x +dx[i]
            ny = y +dy[i]
            if iswall(nx,ny): continue
            if visited[nx][ny] != 0:continue

            if x +ob[i][0] == ex and y+ob[i][1] == ey:## 장애물
                continue

            Q.append((nx,ny))
            visited[nx][ny]=visited[x][y]+1


X,Y = map(int,input().split())
sx,sy, ex,ey = map(int,input().split())
sx -=1
sy -=1
ex -=1
ey -=1

visited = [   [0]*Y  for i in range(X)]

dx=[1, 2, 2, 1, -1, -2, -2, -1]
dy=[2, 1, -1, -2, -2, -1, 1, 2]
ob=[(0,1),(1,0),(1,0),(0,-1),(0,-1),(-1,0),(-1,0),(0,1)]
print(bfs(sx,sy,ex,ey))