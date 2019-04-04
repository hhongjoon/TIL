def iswall(x,y):
    if x>-1 and y>-1 and x<13 and y<5:
        return False
    return True


def bfs(x,y,cnt,bomb,bcnt):
    Q = []
    Q.append((x,y,cnt,bomb,bcnt))
    while len(Q)>0:

        x,y,cnt,bomb,bcnt = Q.pop(0)
        # print(x, y, len(Q))
        if x == 0:
            global maxcnt

            if maxcnt < cnt:
                maxcnt = cnt

            continue

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny):continue

            if bomb == 0 and bcnt>1 and bcnt<6:  # 폭탄진행중
                if mat[nx][ny] == '*':
                    if visited[0][bcnt-1][nx][ny] < cnt + 10:
                        visited[0][bcnt - 1][nx][ny] = cnt + 10
                        Q.append((nx, ny, cnt + 10, bomb, bcnt-1))

                if mat[nx][ny] == 'X' or mat[nx][ny]==0:
                    if visited[0][bcnt-1][nx][ny] < cnt:
                        visited[0][bcnt - 1][nx][ny] = cnt
                        Q.append((nx, ny, cnt, bomb, bcnt-1))


                # if mat[nx][ny] == 0:
                #     Q.append((nx, ny, cnt, bomb, bcnt-1))
                #     visited[0][bcnt - 1][nx][ny] = cnt

                continue

            elif bomb == 0 and bcnt==1: # 폭탄끝

                if mat[nx][ny] == '*':
                    if visited[0][bcnt][nx][ny] < cnt + 10:
                        visited[0][bcnt][nx][ny] = cnt + 10
                        Q.append((nx, ny, cnt + 10, bomb, bcnt))


                if mat[nx][ny] == 'X':
                    if visited[0][bcnt][nx][ny] < cnt -7:
                        visited[0][bcnt][nx][ny] = cnt -7
                        Q.append((nx, ny, cnt - 7, bomb, bcnt))


                if mat[nx][ny] == 0:
                    if visited[0][bcnt][nx][ny] < cnt:
                        visited[0][bcnt][nx][ny] = cnt
                        Q.append((nx, ny, cnt, bomb, bcnt))

                continue


            else: # 폭탄 터지기 전

                if bomb == True:

                    if mat[nx][ny] == '*':
                        if visited[0][bcnt-1][nx][ny] < cnt + 10:
                            visited[0][bcnt - 1][nx][ny] = cnt + 10
                            Q.append( (nx,ny,cnt+10,False,bcnt-1) )


                    if mat[nx][ny] == 'X' or mat[nx][ny] == 0:
                        if visited[0][bcnt - 1][nx][ny] < cnt:
                            visited[0][bcnt - 1][nx][ny] = cnt
                            Q.append( (nx,ny,cnt,False,bcnt-1) )



                if mat[nx][ny] == '*':
                    if visited[1][bcnt][nx][ny] < cnt+10:
                        visited[1][bcnt][nx][ny] = cnt + 10
                        Q.append((nx,ny,cnt+10,bomb,bcnt))


                if mat[nx][ny] == 'X':
                    if visited[1][bcnt][nx][ny] < cnt -7:
                        visited[1][bcnt][nx][ny] = cnt - 7
                        Q.append((nx, ny, cnt - 7,bomb,bcnt))


                if mat[nx][ny] == 0:
                    if visited[1][bcnt][nx][ny] < cnt:
                        visited[1][bcnt][nx][ny] = cnt
                        Q.append((nx, ny, cnt,bomb,bcnt))


                continue




T = int(input())
for _ in range(T):
    mat= [ list(map(lambda x: int(x) if x.isdigit() else str(x),input())) for i in range(13) ]
    # print(mat)
    dx=[-1,-1,-1]
    dy=[1,0,-1]
    st = (12,2)
    maxcnt = -9999999
    visited=[ [0]*7 for i in range(2)]
    for i in range(2):
        for j in range(7):
            visited[i][j] = [ [-9999]*5 for i in range(13) ]

    # print(visited)
    bfs(st[0],st[1],0,1,6)
    print(maxcnt)