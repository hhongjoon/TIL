def iswall(x,y):
    if x>-1 and y>-1 and x<10 and y<9:
        return False
    return True


def bfs(xs,ys,xk,yk):
    temp=[]
    temp.append((xs,ys))
    visited[xs][ys] = 1
    while len(temp)>0:
        loc = temp.pop(0)
        x = loc[0]
        y = loc[1]
        for i in range(8):
            nx = x +dx[i]
            ny = y +dy[i]
            if iswall(nx,ny): continue
            if visited[nx][ny] != 0: continue
            ob = False
            for j in wall[i]:
                if xk == x+j[0] and yk == y+j[1]:
                    ob=True
            if ob == True:
                continue

            temp.append((nx,ny))
            visited[nx][ny] = visited[x][y]+1
            if nx==xk and ny==yk:
                return visited[nx][ny] -1

    return -1

xs,ys = map(int,input().split())
xk, yk = map(int,input().split())
dx=[-2, 2, 3, 3, 2, -2, -3, -3]
dy=[3, 3, 2, -2, -3, -3, -2, 2]


wall=[[(0,1),(-1,2)],[(0,1),(1,2)],[(1,0),(2,1)],[(1,0),(2,-1)],[(0,-1),(1,-2)],[(0,-1),(-1,-2)],[(-1,0),(-2,-1)],[(-1,0),(-2,1)]]

visited = [ [0]*9 for i in range(10) ]
jang = bfs(xs,ys, xk,yk)

print(jang)