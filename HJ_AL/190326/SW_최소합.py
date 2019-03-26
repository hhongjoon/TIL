import sys
sys.stdin = open('최소합.txt')

def iswall(x,y):
    global size
    if x>-1 and y>-1 and x<size and y<size:
        return False
    return True

def cal_min(n,k,dis,loc):
    global mindis
    if dis>mindis:
        return
    if n == k:
        if mindis>dis:
            mindis=dis
        return
    else:
        x = loc[0]
        y = loc[1]
        for i in range(2): # 오 아
            nx = x+dx[i]
            ny = y+dy[i]
            if iswall(nx,ny):
                continue
            plus = mat[nx][ny]
            cal_min(n,k+1,dis+plus,(nx,ny))



T = int(input())
for _ in range(T):
    size = int(input())
    mat = [ list(map(int,input().split())) for i in range(size) ]
    dx=[0,1]
    dy=[1,0]
    st = (0,0)
    mindis = 9999999
    cal_min((size-1)*2,0,mat[0][0],st)
    print("#{} {}".format(_+1,mindis))