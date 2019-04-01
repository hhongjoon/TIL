# DFS인데 나누는 경우의 수가 많음
# if문으로 분기해서 경우마다 재귀 진행


def iswall(x,y):
    if x>-1 and y>-1 and x<N and y<N:
        return False
    return True
def find_path(loc,k,mat_p,dis):
    x = loc[0]
    y = loc[1]
    global maxdis
    if maxdis < dis:
        maxdis = dis
        # print(dis)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if iswall(nx,ny): continue
        if mat_p[nx][ny] == 100:
            continue
        if k==False and mat_p[nx][ny] >= mat_p[x][y]: continue

        if k==True:
            if mat_p[nx][ny] < mat_p[x][y]:
                temp = [mat_p[i][:] for i in range(N)]
                temp[x][y] = 100
                find_path((nx, ny), k, temp, dis + 1)

            for j in range(1, K+1):
                if mat_p[x][y] <= mat_p[nx][ny] - j:
                    continue
                else:
                    temp = [ mat_p[i][:] for i in range(N) ]
                    temp[nx][ny] = temp[nx][ny]-j
                    temp[x][y] = 100
                    find_path((nx,ny),False,temp,dis+1)
        else:  # False 일 때
            if mat_p[nx][ny] < mat_p[x][y]:
                temp = [mat_p[i][:] for i in range(N)]
                temp[x][y] = 100
                find_path((nx, ny), k, temp, dis + 1)

T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    mat = [  list(map(int,input().split()))  for i in range(N) ]
    locs=[]
    maxval = -1
    for i in range(N):
        for j in range(N):
            if mat[i][j] >= maxval:
                if mat[i][j] == maxval:
                    pass
                else:
                    locs.clear()
                locs+=[(i,j)]
                maxval = mat[i][j]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    maxdis = -1
    for i in locs:
        find_path(i,True,mat,0)
    print("#{} {}".format(_+1,maxdis+1))

