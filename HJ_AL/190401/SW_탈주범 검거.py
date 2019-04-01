
def dfs(locx,locy,t):
    Q = []
    visited[locx][locy] = 1
    Q.append((locx,locy,1))
    while len(Q)>0:
        temp = Q.pop()
        x = temp[0]
        y = temp[1]
        time = temp[2]
        for i in range(4):






T = int(input())
for _ in range(1,T+1):
    X,Y, locx,locy,L = map(int,input().split())
    X -=1
    Y-=1
    locx-=1
    locy-=1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [ [0]*Y for i in range(X) ]
    datas = [ [(1,3,6,7),(1,2,4,7),(1,3,4,5),(1,2,5,6)], [(),(2,1,4,7),(),(2,1,5,6)],[(1,3,6,7),(),(1,3,4,5),()] ,[(1,3,6,7),(),(),(1,2,5,6)] ,[(1,3,6,7),(1,2,4,7),(),()] ,[(),(1,2,4,7),(1,3,4,5),()] ,[(),(),(1,3,4,5),(1,2,5,6)]  ]
