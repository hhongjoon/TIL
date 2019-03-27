def iswall(x,y):
    global X,Y
    if x>-1 and y>-1 and x<X and y<Y:
        return False
    return True
def cal():
    while len(temp)>0:
        loc = temp.pop(0)
        x = loc[0]
        y = loc[1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if iswall(nx,ny): continue
            if mat[nx][ny] != 0: continue
            if (nx,ny) not in visited:
                visited.append((nx,ny))
                temp.append((nx,ny))
                mat[nx][ny]=mat[x][y]+1
                aa = mat[nx][ny]


    return aa-1

# 시작
Y , X = map(int,input().split())
mat = [   list(map(int,input().split()))   for i in range(X)   ]

visited=[]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
allt = True
for i in range(X):
    for j in range(Y):
        if mat[i][j] == 1:
            visited.append((i,j))
        if mat[i][j] == 0:
            allt = False

if allt:
    print(0)
else:
    temp=visited[:]
    res = cal()


    allred=True
    for i in range(X):
        for j in range(Y):
            if mat[i][j] == 0:
                allred = False


    if allred == False:
        print(-1)
    else:
        print(res)