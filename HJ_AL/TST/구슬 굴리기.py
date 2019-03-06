def iswall(x,y):
    if x>-1 and  y>-1 and x<row and y <row:
        return False
    return True

def find_path(x,y):
    count = 1
    pivot = 0
    i = order[pivot]-1
    mat[x][y]=3
    while True:
        # print(x,y)
        if iswall(x+dx[i],y+dy[i]) or mat[x+dx[i]][y+dy[i]] == 1:
            pivot+=1
            if pivot == len(order):
                break
            i = order[pivot]-1
            continue


        if mat[x+dx[i]][y+dy[i]] == 0:
            count+=1
            mat[x + dx[i]][y + dy[i]] = 3
            x += dx[i]
            y += dy[i]

            continue

        if mat[x+dx[i]][y+dy[i]] == 3:
            x += dx[i]
            y += dy[i]



    return count

col, row = map(int,input().split())
mat = []
for i in range(row):
    mat.append(list(map(int,input())))
L = int(input())
order = list(map(int,input().split()))
# print(mat)

## 구슬 위치
for i in range(row):
    for j in range(col):
        if mat[i][j] == 2:
            locx,locy = i,j
            break

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(find_path(locx,locy))