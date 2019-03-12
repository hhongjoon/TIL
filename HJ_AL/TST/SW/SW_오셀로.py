#돌사이에 넣을 수 있음/ 세로 가로 대각선
# 보드에 빈곳 없거나 돌을 놓을 곳이 없을 때 -> 돌의 갯수 많은 사람
def iswall(x,y):
    if x>0 and y>0 and x<size+1 and y<size+1:
        return False
    return True



def find_loc(x,y,dol,i):
    global pin
    if not iswall(x,y) and mat[x][y] != 0 and mat[x][y] != dol:
        find_loc(x+dx[i],y+dy[i],dol,i)
        if pin == True:
            mat[x][y] = dol
    elif mat[x][y] == dol:
        pin=True
    elif mat[x][y] == 0:
        return

def score():
    w =0
    b =0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1:
                b+=1
            if mat[i][j] == 2:
                w+=1

    return w, b



def deltafind(x,y,dol):  # 놓을 곳이 있으면 재귀로 다 뒤집는다.
    for i in range(8):
        global pin
        pin = False
        nx = x +dx[i]
        ny = y +dy[i]
        find_loc(nx,ny,dol,i)  # 무조건 들어감
        mat[x][y] = dol

    return False


def cal(x,y,dol):
    # 판 검사 ( 넣을 수 있는지 / 없다면 리턴)  / 돌두기까지
    flag = False
    flag =  deltafind(x,y,dol)   # 놓을 곳이 있다. => 바꾸고 나옴
    if flag == False:  # 놓을 곳이 없으니 상대팀에게 넘김
        return


T= int(input())
for _ in range(T):
    global size
    size, chance = map(int,input().split())
    mat = [  [0]*(size+2)  for i in range(size+2)  ]

    mat[size//2][size//2] = mat[(size//2) +1][(size//2) +1]  = 2
    mat[size // 2 +1][size // 2] = mat[(size // 2)][(size // 2) + 1] = 1
    # print(mat)

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]


    for i in range(chance):
        y, x ,dol = map(int,input().split())
        cal(x,y,dol)

    s_w, s_b = score()

    print("#{} {} {}".format(_+1,s_b,s_w))
