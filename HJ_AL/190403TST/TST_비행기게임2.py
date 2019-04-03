
def iswall(x,y):
    if x>-1 and y>-1 and x<13 and y<5:
        return False
    return True

def bfs(x,y,cnt):
    Q = []
    Q.append((x,y,cnt))
    while len(Q)>0:
        x,y,cnt = Q.pop()
        # print(x,y,len(Q))
        if x ==0:
            global maxcnt
            maxcnt = max(maxcnt,cnt)
            continue
        if dp[x][y] > cnt:
            continue

        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]
            if iswall(nx,ny): continue
            if mat[nx][ny] == 0:
                Q.append((nx,ny,cnt))
                dp[nx][ny] = cnt
            if mat[nx][ny] == '*':
                Q.append((nx,ny,cnt+10))
                dp[nx][ny] = cnt +10
            if mat[nx][ny] == 'X':
                Q.append((nx,ny,cnt-7))
                dp[nx][ny] = cnt - 7




T = int(input())
mat = [  list(map(lambda x: int(x) if x.isdigit() else str(x),input())) for i in range(13) ]

maxsum = -1
for i in range(0,13-5 +1):
    summ = 0
    for j in range(5):
        summ+=mat[i+j].count('X')
    if maxsum<=summ:
        maxsum = summ
        maxidx = i

for i in range(5):
    for j in range(len(mat[0])):
        if mat[maxidx+i][j] == 'X':
            mat[maxidx+i][j] = 0
# print(mat)
dx=[-1,-1,-1]
dy=[1,0,-1]
maxcnt = -999999999

dp = [ [0]*5 for i in range(13) ]
bfs(12,2,0)
print(maxcnt)