def iswall(x,y):
    if x>0 and y>0 and x<size-1 and y<size-1:
        return False
    return True


def findpath(x,y,i,pathM,flag):

    while True:
        if iswall(x,y) and mat[x][y]==0:
            flag=True
            pathM.append((x,y))
            return pathM, flag
        if mat[x][y] == 1 or (x,y)in pathM:
            return pathM, flag
        if mat[x][y] == 0:
            pathM.append((x,y))
            x+= dx[i]
            y+= dy[i]

def cal(I,C,M):     # 인풋,카운트, 지도좌표


    if I == len(cores):
        if C >= maxcnt:
            global maxcnt
            ans.append((C,len(M)))
            maxcnt = C
            # print(M, len(M))
        return
    global cores, dx, dy
    now = cores[I]
    x = now[0]
    y = now[1]

    # if iswall(x, y):                  # 입력값을 가장자리 제외
    #     return cal(I + 1, C + 1, M)

    for i in range(4):

        copyM = M[:]
        # print(x, y, copyM)
        nx = x+dx[i]
        ny = y+dy[i]

        flag = False
        result = findpath(nx,ny,i,copyM,flag)
        if result[1] == True:


            # print(x,y,tempM)
            cal(I+1,C+1,result[0])

        else:
            # print(x, y, M)
            cal(I+1,C,M)


T = int(input())
for _ in range(T):
    global size
    size = int(input())
    mat = [ list(map(int,input().split())) for i in range(size)  ]
    # print(mat)
    dx=[0, 1, 0, -1]
    dy=[1, 0, -1, 0]

    cores = []

    for i in range(1,size-1):
        for j in range(1,size-1):
            if mat[i][j] == 1:
                # print(i,j,'안풋')
                cores.append((i,j))
    temp=[]
    ans=[]
    global maxcnt
    maxcnt = -1

    cal(0,0,temp)

    goal_ea = ans[-1][0]

    mingoal = 99999999
    for i in ans:
        if i[0] == goal_ea:
            if i[1]<mingoal:
                mingoal = i[1]


    print("#{} {}".format(_+1,mingoal))

