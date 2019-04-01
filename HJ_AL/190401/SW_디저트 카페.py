# 한쪽방향으로만 진행
# 가던 길 우선 진행
# 꺾는 횟수를 카운트해서 4각형 만들어지면 끝나도록



def iswall(x,y):
    if x>-1 and y>-1 and x<N and y<N:
        return False
    return True

def dfs(x,y,piv,menus,cnt,cur):
    # global mat, visited, dx, dy
    global xs, ys, maxcnt
    if cur >4:
        return


    if piv != 0 and x==xs and y == ys:
        if maxcnt<cnt:
            maxcnt = cnt
            return

    if visited[x][y] == True:
        return
    if menus[mat[x][y]] != 0:
        return
    menus[mat[x][y]] += 1
    visited[x][y] = True
    nx = x + dx[piv]
    ny = y + dy[piv]
    if not iswall(nx,ny):
        temp = menus[:]
        dfs(nx,ny,piv,temp,cnt+1,cur)

    if piv == 3:
        piv = -1
    nx = x + dx[piv+1]
    ny = y + dy[piv+1]
    if not iswall(nx,ny): # 꺾을 때
        temp = menus[:]
        dfs(nx,ny,piv+1,temp,cnt+1,cur+1)

    visited[x][y] = False




T = int(input())
for _ in range(T):
    N = int(input())
    mat = [ list(map(int,input().split())) for k in range(N) ]

    dx=[1, -1, -1, 1]
    dy=[1, 1, -1, -1]
    maxcnt = -1
    for i in range(1,N-1):
        for j in range(N-1):
            visited = [[False] * N for i in range(N)]
            kinds = [0]*101
            xs = i
            ys = j
            dfs(i,j,0,kinds,0,0)
    print("#{} {}".format(_+1,maxcnt))


