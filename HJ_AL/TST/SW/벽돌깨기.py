import copy

def iswall(a,b):
    if a>-1 and b>-1 and a<x and b<y:
        return False
    return True

def brkruc(a,b,size, temp,cnt):  # 1보다 클 때만 들어옴
    # print(a,b)

    if size == 0:
        return cnt

    cnt += 1
    temp[a][b] = 0
    if size == 1:
        return cnt

    for i in range(4): # 오 아 왼 위
        nx = a + dx[i]
        ny = b + dy[i]
        for k in range(size-1):
            if iswall(nx,ny):
                break
            cnt = brkruc(nx,ny,temp[nx][ny],temp ,cnt)
            nx += dx[i]
            ny += dy[i]
    return cnt


def brk(b,temp,cnt):   # y 위치 주고재귀로 부숨 그리고 정렬까지
    for i in range(x-1,-1,-1):
        if temp[i][b] != 0:
            now = i
            size_b = temp[i][b]
            break
        if i == 0:
            return 0

    # 위치, 크기까지
    orgtemp = copy.deepcopy(temp)

    cnt = brkruc(now,b,size_b, temp,cnt)

    # 확인
    # 정렬 단계
    for i in range(y):
        n = []
        n_com = []
        for p in range(x):
            n.append(orgtemp[p][i])
            n_com.append(temp[p][i])
        if n == n_com:
            continue

        for j in range(x):
            if temp[j][i] == 0:
                for k in range(j+1,x):
                    if temp[k][i] != 0:
                        temp[j][i], temp[k][i] = temp[k][i], temp[j][i]
                        break
    # #확인
    # for i in range(x):
    #     print(temp[i])
    return cnt

def cal(nums, temp, cnt):
    nums+=1
    cntt=cnt
    while nums<=N:
        for j in range(y):
            tempp = copy.deepcopy(temp)
            cntt = brk(j,tempp,cnt)
            cal(nums,tempp,cntt)
        break
    global maxcnt
    if cntt >= maxcnt:
        maxcnt = cntt
    global ea
    ea+=1
    print(ea, cntt,'cnt')
    # #확인
    # for i in range(x):
    #     print(temp[i])
    # return


T = int(input())
for _ in range(T):
    global N, y, x
    N, y, x = map(int,input().split())
    mat = [0]*x
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(x-1,-1,-1):
        mat[i] = list(map(int,input().split()))
    # 확인
    cnt = 0
    nums = 0
    maxcnt = -1
    ea = 0
    cal(nums,mat,cnt)
    print(maxcnt)

