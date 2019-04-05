def iswall(x,y):
    if -1<x<N and -1<y<N:
        return False
    return True

def cal(locs):
    visited = [ mat[i][:] for i in range(N) ]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for loc in locs:
        x,y = loc
        visited[x][y]=1
        for i in range(4):
            tx = x
            ty = y
            for j in range(1,R+1): ## 가로,세로 찍기
                nx = tx + dx[i]
                ny = ty + dy[i]

                if iswall(nx,ny):break
                visited[nx][ny]=1

                ## 0,2번일 때 위아래로찍기
                if i==0 or i==2:
                    kx = nx
                    ky = ny
                    for k in range(R-j):
                        kkx = kx + dx[1]
                        kky = ky + dy[1]
                        if iswall(kkx,kky):break
                        visited[kkx][kky] = 1
                        kx = kkx
                        ky = kky
                    kx = nx
                    ky = ny
                    for k in range(R-j):
                        kkx = kx + dx[3]
                        kky = ky + dy[3]
                        if iswall(kkx,kky):break
                        visited[kkx][kky] = 1
                        kx = kkx
                        ky = kky
                tx = nx
                ty = ny



    cnt=0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                cnt+=1

    global polscnt
    return cnt - polscnt


def powerset(n,k, c):
    if c == 2:
        # print(A)
        #계산
        res = cal(A)

        global maxres
        maxres = max(maxres,res)
        return
    if n == k:
        return
    else:
        A[c] = datas[k]
        powerset(n,k+1, c+1)
        A[c] = 0
        powerset(n,k+1,c)



N = int(input())
R = int(input())
mat = [ list(map(int,input().split())) for i in range(N)]

datas= []
polscnt = 0
for i in range(N):
    for j in range(N):
        datas.append((i,j))
        if mat[i][j] == 1:
            polscnt+=1


A = [0]*2
maxres = -1
powerset(len(datas),0,0)
print(maxres)