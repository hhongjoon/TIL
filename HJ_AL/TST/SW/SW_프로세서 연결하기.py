def iswall(x,y):
    if x>0 and y>0 and x<size-1 and y<size-1:
        return False
    return True



def findloc(x,y,i):



    pass
def cal_overlap():

    while len(overlap)>0:
        temp = []
        (x,y) = overlap.pop()
        for i in range(len(cores)):
            if iswall(cores[i][0],cores[i][1]):
                continue
            if cores[i][0] == x:
                temp.append(cores[i])
                continue
            if cores[i][1] == y:
                temp.append(cores[i])
        if len(temp) == 2:





        print(temp)



    pass

def marking(x,y,i,cnt):
    for a in range(cnt):
        nx = x+dx[i]
        ny = y+dy[i]
        mat[nx][ny] = 2



def count(x,y,i):
    # print(x,y)
    if iswall(x,y) and mat[x][y]==0:
        global flag
        flag = True
        return 1

    if mat[x][y] == 0:
        return 1+ count(x+dx[i],y+dy[i],i)

    if mat[x][y] == 1:
        return 0
    if mat[x][y] == 2:
        overlap.append((x,y))

        return 0



def cal(x,y):
    if iswall(x,y):
        return
    counts =[99]*4
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        global flag
        flag = False
        cnt = count(nx,ny,i)

        if flag == True:
            counts[i] = cnt

    mark = counts.index(min(counts))
    if min(counts) != 99:
        global resultsum
        # print(min(counts),'@@@@@@@@')
        resultsum+=min(counts)

        marking(x,y,mark, min(counts))



T = int(input())
for _ in range(T):
    global size
    size = int(input())
    mat = [ list(map(int,input().split())) for i in range(size)  ]
    # print(mat)
    dx=[0, 1, 0, -1]
    dy=[1, 0, -1, 0]
    global resultsum
    resultsum = 0
    cores = []
    overlap=[]
    for i in range(size):
        for j in range(size):
            if mat[i][j] == 1:
                # print(i,j,'안풋')
                cores.append((i,j))
                cal(i,j)

    print(overlap,'overlap')
    cal_overlap()
    print(cores,'core')




    print("#{} {}".format(_+1,resultsum))