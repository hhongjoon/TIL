def iswall(x,y):
    if x>-1 and y>-1 and x<N and y<N:
        return False
    return True

def dfs(x,y,bomb,h,path):
    Q = [(x,y,bomb,h,path)]
    while Q:
        global maxpath
        temp = Q.pop()
        x,y,bomb,h,path = temp
        maxpath = max(maxpath,len(path))
        # print(temp)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if iswall(nx,ny):continue
            # 산 깎는 경우
            if bomb == 1:
                for i in range(1,K+1):
                    if mat[nx][ny] - i < h:
                        if (nx,ny) not in path:
                            Q.append((nx, ny, 0, mat[nx][ny] - i, path + [(nx,ny)]))

            if mat[nx][ny] < h:
                if (nx, ny) not in path:
                    Q.append((nx, ny, bomb, mat[nx][ny], path + [(nx, ny)]))

T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    mat = [ list(map(int,input().split())) for i in range(N) ]
    tops = []
    maxtop = -1
    for i in range(N):
        for j in range(N):
            if mat[i][j] >= maxtop:
                if mat[i][j] == maxtop:
                    tops.append((i,j))
                else:
                    tops.clear()
                    tops.append((i,j))
                    maxtop = mat[i][j]
    # print(tops)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    maxpath = -1
    for loc in tops:
        # visited = [ [ [0]*2 for j in range(N) ]     for i in range(N)  ]
        dfs(loc[0],loc[1],1,maxtop,[(loc[0],loc[1])])
    print("#{} {}".format(_+1,maxpath))