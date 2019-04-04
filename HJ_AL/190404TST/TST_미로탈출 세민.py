def solution(x1, y1):

    queue.append([x1,y1,0])
    V[x1][y1][0] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y, z = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx <= R-1 and ny <= C-1:
                if M[nx][ny] == 4:
                    return V[x][y][z]

                if M[nx][ny] == 0 and V[nx][ny][z] == 0:
                    V[nx][ny][z] = V[x][y][z] + 1
                    queue.append([nx,ny,z])

                if z < 3 and M[nx][ny] == 2 and V[nx][ny][z+1] == 0:
                    V[nx][ny][z+1] = V[x][y][z] + 1
                    queue.append([nx,ny,z+1])
    return -1

R, C = map(int, input().split())
M = [list(map(int, input().split())) for i in range(R)]
V = [[[0]*4 for i in range(C)] for i in range(R)]

for i in range(R):
    for j in range(C):
        if M[i][j] == 3:
            x1, y1 = i, j
        if M[i][j] == 4:
            x2, y2 = i, j

queue = []
print(solution(x1, y1))
for i in range(R):
    print(V[i])