def isedge(r,c):
    if mat[r][c-1] ==0 and mat[r-1][c]==0:
        return True
    if mat[r][c-1] ==0 and mat[r+1][c]==0:
        return True
    if mat[r][c+1] ==0 and mat[r-1][c]==0:
        return True
    if mat[r][c+1] ==0 and mat[r+1][c]==0:
        return True

    return False


def iscount(r,c, distance):
    # 네 방향이 1일 때 pass
    if mat[r][c-1] ==1 and mat[r][c+1]==1 and mat[r-1][c]==1 and mat[r+1][c]==1:
        return distance


    if isedge(r,c):
        return distance+2

    return distance + 1




mat = [ [0]*102  for i in range(102) ]
T= int(input())
for _ in range(T):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            mat[y + i][x + j] = 1

# for i in range(100):
#     print(mat[i])
distance = 0

for r in range(1,101):
    for c in range(1,101):
        if mat[r][c] == 1:
            distance = iscount(r,c, distance)

print(distance)