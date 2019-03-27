def iswall(x,y):
    global X,Y
    if x>-1 and y>-1 and x<X and y<Y:
        return False
    return True

def findP(loc):
    cnt = 0
    visited=[]
    visited.append(loc)

    Q=[]
    Q.append(loc)
    while len(Q)>0:
        temp = Q.pop(0)
        cnt += 1
        # print(temp[0], temp[1], cnt)
        global gy,gx
        if temp == (gx, gy):
            return mat[gx][gy]
        # mat[temp[0]][temp[1]] = 1

        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if iswall(nx,ny) or mat[nx][ny] != 0 : continue

            if (nx,ny) not in visited:
                visited.append((nx,ny))
                Q.append((nx,ny))
                mat[nx][ny] = mat[temp[0]][temp[1]]+1



Y, X = map(int,input().split())
sy, sx, gy, gx = map(int,input().split())
sy-=1
sx-=1
gy-=1
gx-=1
mat = [ list(map(int,input())) for i in range(X) ]
# print(mat)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
st = (sx,sy)
print(findP(st))