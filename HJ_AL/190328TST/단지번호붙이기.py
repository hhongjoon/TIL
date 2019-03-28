def iswall(x,y):
    if x>-1 and y>-1 and x<N and y<N:
        return False
    return True

def bfs(loc):
    cnt=1
    Q=[]
    Q.append(loc)
    while len(Q)>0:
        temp = Q.pop(0)
        x = temp[0]
        y = temp[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny): continue
            if mat[nx][ny] == 0: continue
            cnt+=1
            Q.append((nx,ny))
            mat[nx][ny] = 0
    return cnt



N = int(input())
mat= [ list(map(int,input()))  for i in range(N) ]
# print(mat)

visited = [ [0]*N for i in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

total = 0
nums=[]
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            total+=1
            mat[i][j] = 0  ## 바꿔줌
            nums.append(bfs((i,j)))
print(total)
nums.sort()
for i in nums:
    print(i)