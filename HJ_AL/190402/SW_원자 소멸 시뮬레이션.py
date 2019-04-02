def iswall(x,y):
    if x>-2001 and y>-2001 and x<2001 and y<2001:
        return False
    return True

def cal():
    bomb = 0
    while len(datas)>0:
        i=0
        atomset=set()
        atoms2 = []
        while i<len(datas):
            # print(datas[i])
            x,y,dr,k = datas[i]
            nx = x+dx[dr]
            ny = y+dy[dr]
            if iswall(nx,ny):
                datas.pop(i)
                continue
            datas[i][0] = nx
            datas[i][1] = ny
            ato  = len(atomset)
            atomset.add((nx, ny))
            if len(atomset) == ato:
                atoms2.append((nx,ny))

            i+=1

        if atoms2:
            for j in atoms2:
                x,y = j
                for k in range(len(datas)-1,-1,-1):
                    if datas[k][0] == x and datas[k][1] == y:
                        bomb+=datas[k][3]
                        datas.pop(k)
    return bomb



            # flag = False
            # for j in range(i+1,len(datas)):
            #     if dr == 0: #위로가는 경우
            #         if datas[j][2] != 1 or datas[j][0] != x:
            #             continue
            #         if datas[j][1] - y <=1:
            #             bomb += datas[j][3]
            #             datas.pop(j)
            #             flag = True
            #
            #             break
            #
            #     if dr == 1: # 아래
            #         if datas[j][2] != 0 or datas[j][0] != x:
            #             continue
            #         if y - datas[j][1] <=1:
            #             bomb += datas[j][3]
            #             datas.pop(j)
            #             flag = True
            #             break
            #     if dr == 2: #왼쪽
            #         if datas[j][2] != 3 or datas[j][1] != y:
            #             continue
            #         if x - datas[j][0]<=1:
            #             bomb += datas[j][3]
            #             datas.pop(j)
            #             flag = True
            #             break
            #     if dr == 3: # 오른쪽
            #         if datas[j][2] != 2 or datas[j][1] != y:
            #             continue
            #         if datas[j][0] - x <=1:
            #             bomb += datas[j][3]
            #             datas.pop(j)
            #             flag = True
            #             break
            # if flag:
            #     bomb += k
            #     datas.pop(i)
            #     continue
    #         datas[i][0]=x
    #         datas[i][1]=y
    #         i+=1
    # return bomb

T = int(input())
for _ in range(1,T+1):
    N = int(input())

    dx=[0, 0, -1, 1]  # 상하좌우
    dy=[1, -1, 0, 0]
    datas=[]
    for i in range(N):
        x,y,dr,k = map(int,input().split())

        datas.append([2*x,2*y,dr,k])

    print("#{} {}".format(_,cal()))


