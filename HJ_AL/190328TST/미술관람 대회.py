def iswall(x,y):
    if x>-1 and y>-1 and x<N and y<N:
        return False
    return True


def unnomal(a,b):
    flag = False
    Q = []
    Q.append((a, b))
    chk = mat[a][b]
    if chk in ['R','G']:
        flag=True
    visited[a][b] = 1
    while len(Q) > 0:
        temp = Q.pop(0)
        x = temp[0]
        y = temp[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx, ny): continue
            if visited[nx][ny] == 1: continue

            if flag:
                if mat[nx][ny] in ['R','G']:
                    Q.append((nx, ny))
                    visited[nx][ny] = 1
            else:
                if mat[nx][ny] == chk:
                    Q.append((nx, ny))
                    visited[nx][ny] = 1
    pass

def nomal(a,b):
    Q = []
    Q.append((a,b))
    chk = mat[a][b]
    visited[a][b] = 1
    while len(Q)>0:
        temp = Q.pop(0)
        x = temp[0]
        y = temp[1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if iswall(nx,ny):continue
            if visited[nx][ny] == 1: continue
            if mat[nx][ny] == chk:
                Q.append((nx,ny))
                visited[nx][ny]=1
    pass


N = int(input())
mat = [  list(map(str,input()))  for i in range(N)   ]
# print(mat)

visited=[ [0]*N for i in range(N) ]

dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            cnt+=1
            nomal(i,j)


visited=[ [0]*N for i in range(N) ]
cntt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            cntt+=1
            unnomal(i,j)
print(cnt,cntt)
