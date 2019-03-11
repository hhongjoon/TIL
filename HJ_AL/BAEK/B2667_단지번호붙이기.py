def iswall(x,y):
    if x>-1 and y>-1 and x<size and y<size:
        return False
    return True

def house(x,y):
    check = 1
    temp=[]
    visited.append((x,y))
    temp.append((x,y))
    while len(temp)>0:
        loc = temp.pop()
        x = loc[0]
        y = loc[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny) or mat[nx][ny] == 0:
                continue
            if mat[nx][ny] == 1 and (nx,ny) not in visited:

                temp.append((nx,ny))
                visited.append((nx,ny))
                check+=1
    return check



size = int(input())
mat = [  list(map(int,input()))   for i in range(size) ]

dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]
visited=[]
cnt = 0
checks = []
for i in range(size):
    for j in range(size):
        if (i,j) not in visited and mat[i][j] == 1:
            # print(i,j)
            cnt+=1
            checks.append(house(i,j))

print(cnt)
checks.sort()
for i in checks:
    print(i)