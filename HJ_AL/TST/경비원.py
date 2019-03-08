def cal_len(start,goal):
    visited=[]
    temp=[]
    visited.append(start)
    temp.append(start)
    cnt = 0
    while len(temp) > 0:
        for i in temp:
            x = i[0]
            y = i[1]
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if not iswall(nx,ny) and (nx,ny) not in visited:
                    visited.append((nx,ny))
                    temp.append((nx,ny))
        cnt+=1


    pass

def iswall(x,y):
    if x>-1 and y>-1 and x<row and y<col:
        return False
    return True


def find_loc(way, size, M):
    if way == 1:
        mat[0][size] = M
        return (0,size)
    if way == 2:
        mat[row-1][size] = M
        return (row-1, size)
    if way == 3:
        mat[size][0] = M
        return (size, 0)
    if way == 4:
        mat[0][col-1] = M
        return (0, col-1)


global col, row
col, row = map(int,input().split())
nums = int(input())
data = []
mat = [  [0]*col  for i in range(row)  ]
for i in range(1,row-1):
    for j in range(1,col-1):
        mat[i][j] = 1

loc = []
for i in range(nums):
    way , size = map(int,input().split())
    loc.append(find_loc(way,size,3))

print(mat)
way, size = map(int,input().split())
start = find_loc(way,size,5)

dx= [0, 1, 1, -1]
dy= [1, 0, -1, 0]

for i in loc:
    cal_len(start,loc)