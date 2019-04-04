
def bfs(x,y,bomb,cnt):
    Q=[(x,y,bomb,cnt)]

    while len(Q)>0:
        x,y,bomb,cnt = Q.pop(0)
        print(x,y,bomb,cnt, Q)
        global mindis, gx,gy, flag
        if mindis < cnt:
            continue
        if x==gx and y ==gy:
            mindis = min(mindis,cnt)
            flag = True
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if mat[nx][ny]== 1:continue
            if mat[nx][ny]== 0:
                if visited[bomb][nx][ny] > cnt+1:
                    visited[bomb][nx][ny] = cnt+1
                    Q.append((nx,ny,bomb,cnt+1))
                continue
            if mat[nx][ny]== 2:
                if bomb == 0: # 폭탄 없을 때
                    continue
                if visited[bomb-1][nx][ny] > cnt+1:  # 폭탄  쓸 때
                    visited[bomb-1][nx][ny] = cnt+1
                    Q.append((nx,ny,bomb-1,cnt+1))





X, Y = map(int,input().split())
mat = [ list(map(int,input().split())) for i in range(X) ]

for i in range(X):
    for j in range(Y):
        if mat[i][j] == 3:
            sx = i
            sy = j
        if mat[i][j] == 4:
            gx = i
            gy = j
            mat[i][j] = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [0]*4
for i in range(4):
    visited[i] = [ [9999]*Y for i in range(X) ]

mindis = 99999
flag = False
bfs(sx,sy,3,0)
if flag:
    print(mindis)
else:
    print(-1)