def cal_depth(x,y):
    # print(x,y)
    global T
    min_cnt = 100
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        cnt = 0

        while True:
            cnt+=1
            if mat[nx][ny] == 0:
                if min_cnt>=cnt:
                    min_cnt = cnt
                break
            nx += dx[i]
            ny += dy[i]

    return min_cnt


T = int(input())
mat = []
for i in range(T):
    mat.append(list(map(int,input().split())))



dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(1,T-1):
    for j in range(1,T-1):
        if mat[i][j] == 1:
            mat[i][j] = cal_depth(i,j)

sum = 0
for i in range(1,T-1):
    for j in range(1,T-1):
        sum += mat[i][j]
print(sum)



