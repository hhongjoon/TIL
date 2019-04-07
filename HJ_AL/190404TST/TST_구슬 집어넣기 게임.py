"""
R B 구슬을 룰에 따라 구멍에 넣음
DFS사용 이유 : 가장 먼저 골에 도달 하고 나서 가지치기 하려고 / BFS랑 큰차이 없음
4차원 배열로 빨간구슬좌표 파란 구슬 좌표로 갔던 길 (cnt)넣어서 재방문 X

"""

def findnext(x,y,i):
    nx = x +dx[i]
    ny = y +dy[i]
    if mat[nx][ny] == "#":
        return (x,y)
    return (nx,ny)


def dfs(a,b,cnt):
    Q=[(a,b,cnt)]


    while len(Q)>0:
        temp = Q.pop()  # dfs bfs 여기만 바꾸면 됨
        rx, ry = temp[0]
        bx, by = temp[1]
        cnt = temp[2]
        # print(temp)
        global hole, mincnt
        if cnt>mincnt:
            continue
        for i in range(4):
            locA = findnext(rx,ry,i)
            locB = findnext(bx,by,i)


            if locA == hole:
                global flag
                flag = True
                mincnt = min(mincnt,cnt+1)
                continue
            if locA == locB:
                continue
            if locB == hole:
                continue
            if visited[locA[0]][locA[1]][locB[0]][locB[1]] <= cnt + 1:
                continue
            visited[locA[0]][locA[1]][locB[0]][locB[1]] = cnt + 1
            Q.append((locA,locB,cnt+1))


T = int(input())
for _ in range(T):
    X , Y = map(int,input().split())
    mat = [ list(map(str,input())) for i in range(X) ]
    for i in range(X):
        for j in range(Y):
            if mat[i][j] == 'R':
                locR=(i,j)
            if mat[i][j] == 'B':
                locB=(i,j)
            if mat[i][j] == 'H':
                hole = (i,j)
    dx =[0, 1, 0, -1]
    dy=[1, 0, -1, 0]

    visited = [   [0]*Y   for i in range(X)   ]
    for i in range(X):
        for j in range(Y):
            visited[i][j] = [   [9999]*Y   for i in range(X)   ]



    mincnt = 10
    flag = False
    dfs(locR,locB,0)
    if flag:
        print(mincnt)
    else:
        print(-1)