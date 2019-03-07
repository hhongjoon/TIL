size, donut = map(int,input().split())
mat = [  list(map(int,input().split()))  for i in range(size)]
# print(mat)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
maxsum = -1
for i in range(1,size-1):
    for j in range(1,size-1):
        sum = 0
        for k in range(8):
            sum += mat[i+dx[k]][j+dy[k]]
        if sum > maxsum:
            maxsum = sum
print(maxsum)