def iswall(x,y):
    if x>-1 and y>-1 and x<N and y<N:
        return False
    return True

def bfs(x,y):
    Q = []
    visited[x][y] = 1
    Q.append((x,y,mat[x][y]))
    while len(Q)>0:
        temp = Q.pop(0)
        x=temp[0]
        y=temp[1]
        shape=temp[2]
        if shape=='A':
            shape=10
        if shape=='B':
            shape=11
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny): continue # 벽이면 패스
            if datas_s[shape][0][i] == '0': continue  # 보낼 수 없는경우 패스
            if mat[nx][ny] in datas_g[i] and visited[nx][ny] == 0: # 받을 수 있는 경우에 어팬드
                visited[nx][ny]=1
                Q.append((nx,ny,mat[nx][ny]))



N = int(input())
x,y = map(int,input().split())
mat = [ list(map(lambda x: x if x.isalpha() else int(x),input())) for i in range(N) ]
# print(mat)
visited = [ [0]*N for i in range(N) ]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
datas_g = [(1,4,5,8,9,'A','B'),(2,5,6,7,9,'A','B'),(1,3,6,7,8,'A','B'),(2,3,4,7,8,9,'B')]
datas_s = [['0000'],['1010'],['0101'],['1100'],['0110'],['0011'],['1001'],['1101'],['1110'],['0111'],['1011'],['1111']]
bfs(y,x)

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and mat[i][j] != 0:
            cnt+=1
print(cnt)