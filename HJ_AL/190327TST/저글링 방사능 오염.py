def iswall(x,y):
    global X,Y
    if x>-1 and y>-1 and x<X and y<Y:
        return False
    return True

def cal(st):
    visited=[]
    temp=[]
    visited.append((st[0],st[1]))
    temp.append((st[0],st[1]))
    mat[st[0]][st[1]]=3
    while len(temp)>0:
        loc = temp.pop(0)
        x = loc[0]
        y = loc[1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if iswall(nx,ny) or mat[nx][ny] == 0:
                continue
            if (nx,ny) not in visited:
                mat[nx][ny] = mat[x][y] +1
                visited.append((nx,ny))
                temp.append((nx,ny))



Y,X = map(int,input().split())
mat = [ list(map(int,input())) for i in range(X)]
# print(mat)
sY, sX = map(int,input().split())
sY-=1
sX-=1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cal((sX,sY))

remain = 0
maxnum = -1
for i in range(X):
    for j in range(Y):
        if mat[i][j] == 1: remain+=1
        if maxnum < mat[i][j]:
            maxnum = mat[i][j]
print(maxnum)
print(remain)