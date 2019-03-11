def iswall(x,y):
    if x>-1 and y>-1 and x<row and y<col:
        return False
    return True

def findgoal(start,goal):
    x,y = start[0],start[1]
    cnt = 1
    new= []
    new.append((start[0],start[1]))
    while True:
        temp = new
        new = []

        for j in temp:
            # print(j)
            for i in range(4):
                nx = j[0]+dx[i]
                ny = j[1]+dy[i]
                # print(nx,ny)
                if iswall(nx,ny) or mat[nx][ny] == 0:
                    continue

                if mat[nx][ny] == 1:
                    mat[nx][ny] = 0
                    new.append((nx,ny))

        cnt +=1
        # print(new, cnt)
        if (goal[0],goal[1]) in new:
            return cnt



global row, col
row, col = map(int,input().split())
mat= [  list(map(int,input()))  for i in range(row) ]
# print(mat)
start = (0,0)
goal = (row-1,col-1)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(findgoal(start,goal))
