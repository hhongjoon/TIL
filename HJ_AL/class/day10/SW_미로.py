import sys
sys.stdin = open("maze.txt")

def find_enter(size):
    for x in range(size):
        for y in range(size):
            if maze[x][y] == '2':
                return x, y

def isok(enter,size):

    x = enter[0]
    y = enter[1]
    #print(x,y)
    if maze[x][y] == '3':
        maze[x][y]='1'
        global flag
        flag = True
        return
    print(x,y)
    maze[x][y] = '1' ## 방문 했음 표시

    if y + 1 < size and maze[x][y+1] != '1':  # 오른
        enter = (x,y+1)
        isok(enter,size)
    if x + 1 < size and maze[x+1][y] != '1':  # 아래
        enter = (x+1,y)
        isok(enter,size)
    if y - 1 > -1 and maze[x][y-1] != '1':  # 좌
        enter = (x,y-1)
        isok(enter,size)
    if x - 1 > -1 and maze[x-1][y] != '1':  #위
        enter = (x-1,y)
        isok(enter,size)

T = int(input())
for _ in range(T):
    size = int(input())
    maze = [ list(input()) for i in range(size)      ]

    #출발점
    enter = find_enter(size)
    flag = False
    isok(enter,size)
    print(f"#{_+1} {int(flag)}")

