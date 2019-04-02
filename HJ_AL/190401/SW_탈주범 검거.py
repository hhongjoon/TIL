## 왜 bfs는 되고 dfs는 안되지???
## 단계별로 추가라서?

def iswall(x,y):
    if x>-1 and y>-1 and x<X and y<Y:
        return False
    return True


def dfs(locx,locy,t):
    Q = []
    visited[locx][locy] = 1
    shape = mat[locx][locy]
    Q.append((locx,locy,1,shape))
    while len(Q)>0:
        temp = Q.pop(0)
        x = temp[0]
        y = temp[1]
        time = temp[2]
        shape = temp[3]

        if time == t:
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if iswall(nx,ny) or mat[nx][ny] == 0: continue
            if mat[nx][ny] in datas[shape][i]:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    Q.append((nx,ny,time+1,mat[nx][ny]))






T = int(input())
for _ in range(1,T+1):
    X,Y, locx,locy,L = map(int,input().split())

    mat = [ list(map(int,input().split())) for i in range(X)  ]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [ [0]*Y for i in range(X) ]
    datas = [ [],[(1,3,6,7),(1,2,4,7),(1,3,4,5),(1,2,5,6)], [(),(2,1,4,7),(),(2,1,5,6)],[(1,3,6,7),(),(1,3,4,5),()] ,[(1,3,6,7),(),(),(1,2,5,6)] ,[(1,3,6,7),(1,2,4,7),(),()] ,[(),(1,2,4,7),(1,3,4,5),()] ,[(),(),(1,3,4,5),(1,2,5,6)]  ]
    dfs(locx,locy,L)
    summ = 0
    for i in range(len(visited)):
        summ += sum(visited[i])
    print("#{} {}".format(_,summ))