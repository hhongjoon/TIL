
def iswall(x,y):
    if x>-1 and y>-1 and x<X and y<Y:
        return False
    return True

def bfs(x,y,dr,cnt):
    Q=[(x,y,dr,cnt)]

    while len(Q)>0:
        global gx, gy, gdr, mincal
        x,y,dr,cnt = Q.pop(0)
        if cnt > visited[gdr][gx][gy]:
            continue

        # print(x,y,cnt,len(Q))


        # 직선가는 경우
        nx = x
        ny = y
        for i in range(1,4):
            nx += dx[dr]
            ny += dy[dr]
            if iswall(nx,ny) or mat[nx][ny]==1: break
            if visited[dr][nx][ny] <=cnt+1:
                continue
            visited[dr][nx][ny] = cnt + 1
            Q.append((nx,ny,dr,cnt+1))

        # 방향바꾸는 경우
        for i in range(1,5):
            if dr == i:
                continue
            if (dr==1 and i==2) or (dr==2 and i==1) or (dr==3 and i==4) or (dr==4 and i==3):
                continue

            if visited[i][x][y] <=cnt+1:
                continue
            visited[i][x][y] = cnt+1
            Q.append((x, y, i, cnt + 1))



X,Y = map(int,input().split())
mat = [ list(map(int,input().split()))  for i in range(X) ]
sx,sy,sdr = map(int,input().split())
sx-=1
sy-=1
gx,gy,gdr = map(int,input().split())
gx-=1
gy-=1
visited=[0]*5
for i in range(1,5):
    visited[i] = [ [9999]*Y for i in range(X)]

dx = [None, 0, 0, 1, -1]
dy = [None, 1, -1, 0, 0]

mincal = 99999
bfs(sx,sy,sdr,0)
print(visited[gdr][gx][gy])