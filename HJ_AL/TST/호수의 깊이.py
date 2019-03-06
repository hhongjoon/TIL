def cal_depth(x,y):
    min_distance = 100
    for i in range(4):
        distance = 1
        while True:
            if mat[x+dx[i]][y+dy[i]] == 0:
                if min_distance > distance:
                    min_distance = distance
            x += dx[i]
            y += dy[i]
    pass


T = int(input())
mat = []
for i in range(T):
    mat.append(list(map(int,input().split())))
print(mat)
dx = [1,0,-1,0]
dy = [0,-1,0,1]

for i in range(1,T-1):
    for j in range(1,T-1):
        if mat[i][j] == 1:
            mat[i][j] = cal_depth(i,j)






