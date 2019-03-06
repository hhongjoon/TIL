def can_go(pivot,x,y): ## 과일:몸길이 증가 / 1: 위치만 변화 / F
    global snakesize

    if mat[x + dx[pivot]][y + dy[pivot]] == 0 or mat[x + dx[pivot]][y + dy[pivot]] == 3:  # 벽 또는 뱀
        return 'F', x, y

    if mat[x+dx[pivot]][y+dy[pivot]] == 5:         # 먹이일 때
        mat[x + dx[pivot]][y + dy[pivot]] = 3
        x = x+dx[pivot]
        y = y+dy[pivot]
        snakesize.append((x, y))            # 뱀위치. 길이 저장
        return 'T', x, y

    if mat[x+dx[pivot]][y+dy[pivot]] == 1:
        if len(snakesize)>1:
            change = snakesize.pop(0)
            mat[change[0]][change[1]] = 1
            snakesize.append((x+dx[pivot],y+dy[pivot]))

            for j in range(len(snakesize)):
                mat[snakesize[j][0]][snakesize[j][1]] = 3
            x = x + dx[pivot]
            y = y + dy[pivot]
            return 'T',x,y

        else:
            snakesize.pop(0)
            mat[x][y] = 1
            mat[x+dx[pivot]][y+dy[pivot]] = 3
            x = x + dx[pivot]
            y = y + dy[pivot]
            snakesize.append((x,y))
            return 'T', x, y

def next_dir(pivot, act):
    if pivot ==0: # 오
        if act == 'L':
            pivot = 3
        else:
            pivot = 1
    elif pivot ==1:  # 아
        if act == 'L':
            pivot = 0
        else:
            pivot = 2
    elif pivot == 2: # 왼
        if act == 'L':
            pivot = 1
        else:
            pivot = 3
    else : # 위
        if act == 'L':
            pivot = 2
        else:
            pivot = 0
    return pivot

def cal(T, act, pivot,x,y):
    global second
    global flag
    for i in range(T):  ## 초 당 행동
        second +=1    # 초 증가
        result = can_go(pivot,x,y)  # 갈 수 있는지, 먹이가 있는지

        if result[0] == 'F':
            flag=False
            print(second)
            break
        x = result[1]
        y = result[2]
    # 초 끝나면 방향바꿈
    pivot = next_dir(pivot,act)
    return pivot,x,y

def main():
    global mat
    global dx
    global dy

    N = int(input())
    mat = [  [0]*(N+2) for i in range(N+2)   ]
    for i in range(1,N+1):
        for j in range(1,N+1):
            mat[i][j] = 1
    K = int(input())
    for i in range(K): # 먹이 위치
        x, y = map(int,input().split())
        mat[x][y] = 5

    L=int(input())

    dx=[0, 1, 0, -1]
    dy=[1, 0, -1, 0]

    pivot = 0

    global flag
    flag=True
    global second
    second = 0
    global snakesize
    snakesize = [(1,1)]
    x,y = 1,1
    mat[x][y] = 3
    prevtime = 0
    for i in range(L):         ## 명령 입력
        time, act = input().split()
        time = int(time)
        temp = time       # 임시로 빼놓음
        time = time - prevtime

        print(time,temp)
        pivot,x,y = cal(time, act,pivot,x,y)
        prevtime = temp

        for i in range(len(mat)):
            print(mat[i])
        print()


        if flag is False:
            return
    print(second+1)          # 중간에 끝나지 않고 명령을 이수했을 때



if __name__ == "__main__":
    main()
