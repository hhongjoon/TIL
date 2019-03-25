import sys
import copy
sys.stdin = open("프로세서 연결하기_input.txt")

def iswall(x,y):
    if x>0 and y>0 and x<size-1 and y<size-1:
        return False
    return True


def findpath(x,y,i,pathM,flag,cnt):

    while True:
        if iswall(x,y) and pathM[x][y]==0:
            flag=True
            cnt+=1
            pathM[x][y]=2
            return pathM, flag ,cnt
        if pathM[x][y] == 1 or pathM[x][y] == 2:
            return pathM, flag ,cnt
        if pathM[x][y] == 0:
            pathM[x][y]=2
            cnt+=1
            x+= dx[i]
            y+= dy[i]

def cal(I, M,cnt):     # 인풋,카운트, 지도좌표
    global maxcnt

    if I == len(cores):
        if cnt <= maxcnt:

            # ans.append((C,cnt))
            maxcnt = cnt
            # print(M, len(M))
        return

    # global cores, dx, dy
    now = cores[I]
    x = now[0]
    y = now[1]

    # if iswall(x, y):                  # 입력값을 가장자리 제외
    #     return cal(I + 1, C + 1, M)

    for i in range(4):

        copyM = copy.deepcopy(M)
        # copyM = [ M[i][:] for i in range(size)  ]
        # print(x, y, copyM)
        nx = x+dx[i]
        ny = y+dy[i]

        flag = False
        result = findpath(nx,ny,i,copyM,flag,cnt)
        if result[1] == True:

            # tempM = [ result[0][i][:] for i in range(size)]
            # cnt = result[2]
            # print(x,y,plus)
            cal(I+1, result[0],result[2])

        # else:
        #     # print(x, y, cnt)
        #     cal(I+1,C,M,cnt)


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

    # ans=[]
    # global maxcnt
    maxcnt = 10000

    cal(0,mat,0)
    print("#{} {}".format(_+1, maxcnt))
    # print(ans[-1][0])
    # goal_ea = ans[-1][0]
    #
    # mingoal = 99999999
    # for i in ans:
    #     if i[0] == goal_ea:
    #         if i[1]<mingoal:
    #             mingoal = i[1]
    #
    #
    # print("#{} {}".format(_+1,mingoal))