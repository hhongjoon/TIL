def iswall(x,y):
    if x>-1 and y>-1 and x<X and y<Y:
        return False
    return True


def bfs2(x,y,cnt):
    #
    Q = [(x,y,cnt)]
    while Q:
        temp = Q.pop(0)
        x,y,cnt = temp

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if iswall(nx,ny):continue
            if mat[nx][ny] == '.':
                if tempmat[nx][ny] > cnt +1:
                    Q.append((nx,ny,cnt+1))
                    tempmat[nx][ny] = cnt + 1
                continue
            if mat[nx][ny] == 'X':
                return cnt

    return 999999999


def bfs(x,y):
    Q=[(x,y)]

    while Q:
        temp = Q.pop(0)
        x, y = temp
        datas.append((x,y))
        mat[x][y] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if iswall(nx,ny):continue
            if mat[nx][ny] == 'X':
                Q.append((nx,ny))
                mat[nx][ny] =1
    return


X , Y = map(int,input().split())
mat = [ list(map(str,input())) for i in range(X) ]

visited = [ [0]*Y for i in range(X)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
datas=[]
flag = False
for i in range(X):
    for j in range(Y):
        if mat[i][j] =='X':
            bfs(i,j)

            flag = True
            break
    if flag:
        break

tempmat = [ [9999]*Y for i in range(X) ]
mindis = 999999
for loc in datas:
    dis = bfs2(loc[0],loc[1],0)
    mindis = min(mindis,dis)
print(mindis)