def iswall(x,y):
    if x>-1 and y>-1 and x<X and y<Y:
        return False
    return True
def bfs(cr,x,y):
    global mat
    tempmat = [ mat[i][:] for i in range(12) ]
    Q = [(x,y)]
    tempmat[x][y] = '.'
    cnt = 1
    while Q:
        x,y = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny):continue
            if tempmat[nx][ny] == cr:
                Q.append((nx,ny))
                cnt+=1
                tempmat[nx][ny] = '.'
    if cnt>=4:
        global comp
        comp = True
        mat = tempmat



T = int(input())
for _ in range(T):
    X , Y =12, 6
    mat=[ list(map(str,input())) for i in range(12) ]
    # print(mat)
    datas = ['R','G','B','P','Y']

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]


    result = 0
    while True:
        comp = False
        prev = None
        for i in range(11,-1,-1):  # 부심
            for j in range(6):
                if mat[i][j] != prev and mat[i][j] in datas:
                    cr = mat[i][j]
                    bfs(cr,i,j)
                    prev = cr
        if comp:
            result+=1

        ttemp = [ mat[i][:] for i in range(12) ]
        for j in range(6):  # 내려와
            while True:
                room = False
                flag = False
                for i in range(11,0,-1):
                    if mat[i][j] =='.':
                        room=True
                    if mat[i][j] in datas and room:
                        flag = True
                        break
                if not flag:
                    # print('ddd')
                    break
                while True:
                    if i+1 <= 11 and mat[i+1][j] == '.':
                        mat[i][j], mat[i+1][j] = mat[i+1][j], mat[i][j]
                        i = i+1
                        continue
                    break

        # if "".join("".join(row) for row in mat)  == '.'*(12*6):
        #     break
        if ttemp == mat:
            break

    print(result)
