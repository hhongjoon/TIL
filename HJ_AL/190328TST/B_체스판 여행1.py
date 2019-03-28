def iswall(x,y):
    global size
    if x>-1 and y>-1 and x<size and y<size:
        return False
    return True

def markvisit(x,y,mal,level):
    visited[level][mal][x][y]=1

def isvisit(x,y,mal,level):
    if visited[level][mal][x][y] == 1:
        return True
    return False

def gocal(loc,direc,goal,what): # 좌표,나아갈방향(튜플),목표,mal
    x=loc[0]
    y=loc[1]
    nx = x + direc[0]
    ny = y + direc[1]
    path = []
    while True:
        up=False
        if iswall(nx,ny):
            return path

        if mat[nx][ny] == goal:
            # print(nx,ny)
            up=True
        if up:
            if isvisit(nx,ny,what,goal+1):
                pass
            else:
                markvisit(nx,ny,what,goal+1)
                path.append(((nx, ny), goal+1))
        else:
            if isvisit(nx,ny,what,goal):
                pass
            else:
                markvisit(nx,ny,what,goal)
                path.append(((nx, ny), goal))

        nx += direc[0]
        ny += direc[1]

def bfs(st):
    now = st
    Q=[]
    cnt = 0
    Q.append((now,0,None,cnt,2))           # (현재좌표, 말상태, 이전좌표, 움직인 횟수,다음목적지)
    Q.append((now, 1, None, cnt,2))        # 이전!=현재  # 0 룩 / 1 비숍 / 2 나이트
    Q.append((now, 2, None, cnt,2))        # 도달하면 바로 끝
    markvisit(now[0],now[1],0,1)
    markvisit(now[0], now[1], 1,1)
    markvisit(now[0], now[1], 2,1)
    while len(Q)>0:
        temp = Q.pop(0)
        # print(temp)
        now =temp[0]
        mal = temp[1]
        prev = temp[2]
        cnt = temp[3]
        goal = temp[4]

        if goal == size*size+1:
            return cnt


        # 경우의수
        ## 움직이는 경우
        x = now[0]
        y = now[1]
        loc = (x, y)
        if mal == 0:  # 룩
            for i in range(4):  # 4방향 오 아 왼 위
                new = gocal(loc, look[i], goal,0)  # 같은방향에서 갈 수 있는 길 반환, goal에 도달 했는지
                for j in new:
                    Q.append((j[0], mal, loc, cnt + 1, j[1]))

        elif mal == 1:  ## 비숍
            for i in range(4):
                new = gocal(loc, vishop[i], goal,1)
                for j in new:
                    Q.append((j[0], mal, loc, cnt + 1, j[1]))

        else:    ## 나이트
            for i in range(8):
                nx = x + knight[i][0]
                ny = y + knight[i][1]
                if iswall(nx, ny): continue
                # 나이트 이어서 구현 / 이전값 현재값 관리

                if mat[nx][ny] == goal:
                    if isvisit(nx,ny,mal,goal+1):
                        pass
                    else:
                        markvisit(nx,ny,mal,goal+1)

                        Q.append(((nx, ny), mal, loc, cnt + 1, goal + 1))
                else:
                    if isvisit(nx,ny,mal,goal):
                        pass
                    else:
                        markvisit(nx,ny,mal,goal)
                        Q.append(((nx, ny), mal, loc, cnt + 1, goal))

        for i in range(3):
            if isvisit(x,y,i,goal):
                continue
            else:
                markvisit(x,y,i,goal)
                Q.append((now,i,now,cnt+1,goal))

size = int(input())
mat = [ list(map(int,input().split())) for i in range(size)]
flag = False
for i in range(size):
    for j in range(size):
        if mat[i][j]==1:
            st = (i,j)
            flag = True
            break
    if flag:
        break
# print(mat)

look = [(0,1),(1,0),(0,-1),(-1,0)]  # 방향
vishop=[(1,1),(1,-1),(-1,-1),(-1,1)] # 방향
knight=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)] #좌표

visited = [0]*(size*size+2)
for i in range(1,size*size+2):  ##visited[level][mal][x][y]
    visited[i] = [list( [0]*size   for i in range(size) ),list(   [0]*size   for i in range(size)      ),list(   [0]*size   for i in range(size)      )]

result = bfs(st)
print(result)
