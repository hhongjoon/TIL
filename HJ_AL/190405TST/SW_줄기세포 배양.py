
T = int(input())
for _ in range(T):
    X1, Y1, K = map(int,input().split())
    mat = [ list(map(int,input().split())) for i in range(X1) ]

    visited = [ [0]*(Y1+2*K) for i in range(X1+2*K)  ]
    datas = []
    for i in range(X1):
        for j in range(Y1):
            if mat[i][j] != 0:
                visited[K+i][K+j] = [mat[i][j],mat[i][j]]
                datas.append([K+i,K+j,mat[i][j],mat[i][j]])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 0
    while cnt<K:
        tt = []
        ttt = set()
        for i in range(len(datas)):
            x,y,org,imf = datas[i]

            if imf >0:
                datas[i][3] -=1
                visited[x][y][1] -=1
                continue
            if -org<imf and imf <=0: # 활성 상태
                datas[i][3] -=1
                for j in range(4):
                    nx = x+dx[j]
                    ny = y+dy[j]

                    if visited[nx][ny] != 0:
                        continue


                    tt.append([nx,ny,org,org])
                    ttt.add((nx,ny))
                    if len(ttt) != len(tt):
                        for i in range(len(tt)):
                            if tt[i][0] == nx and tt[i][1] == ny:
                                if tt[i][2] > org:
                                    tt.pop()
                                    break
                                else:
                                    tt.pop(i)
                                    break
            if imf <= -org:
                continue
        datas += tt
        for i in tt:
            tx,ty,torg,timf = i
            visited[tx][ty] = [torg,timf]

        cnt +=1


    res = 0
    for i in datas:
        x,y,org,imf = i
        if -org<imf:
            res+=1
    print("#{} {}".format(_+1,res))
