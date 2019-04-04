def bfs():
    dx = [0, 1, 0, -1]  # 동 남 서 북
    dy = [1, 0, -1, 0]
    # 이동
    while Q:
        x, y, d, cnt = Q.pop(0)
        if (x, y, d) == (ex, ey, ed):
            return cnt
        for k in range(1, 4):
            (nx, ny) = (x + dx[d]*k, y + dy[d]*k)
            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if arr[nx][ny]: continue
            if visited[nx][ny]: continue
            Q.append((nx, ny, d, cnt+1))
            Q.append((nx, ny, (d+1) % 4, cnt+2))
            Q.append((nx, ny, (d-1) % 4, cnt+2))
            Q.append((nx, ny, (d+2) % 4, cnt+3))
            visited[nx][ny] = cnt


# main--------------------------------
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())
(sx, sy, ex, ey, sd, ed) = (sx-1, sy-1, ex-1, ey-1, sd-1, ed-1)
# 동서남북 => 동남서북으로 바꾸기
if sd == 1:
    sd = 2
elif sd == 2:
    sd = 1
if ed == 1:
    ed = 2
elif ed==2:
    ed = 1

Q = [(sx,sy,sd,0), (sx, sy, (sd+1)%4, 1), (sx, sy, (sd-1)%4, 1), (sx, sy, (sd+2)%4, 2)]
visited = [[0]*m for _ in range(n)]
visited[sx][sy]=1
print(bfs())
# bfs()
for i in range(n):
    print(visited[i])