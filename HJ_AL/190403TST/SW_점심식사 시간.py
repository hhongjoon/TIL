def cal():
    a=[]
    b=[] # 거리들
    for i in range(len(A)):
        x,y = datas[i]
        if A[i]==0:
            a.append(abs(x-steps[0][0]) + abs(y-steps[0][1]) + 1)
        if A[i] == 1:
            b.append(abs(x - steps[1][0]) + abs(y - steps[1][1]) + 1)


    a.sort()
    b.sort()
    chk = 0
    while True: # b
         ## 최대3명까지 같이
        if chk == 0:
            cnt = b.count(b[0])
            if cnt>3:
                cnt = 3
        else:
            cnt = 0
            for i in range(len(b)):
                if cnt == 3:
                    break
                if steps[1][2] > b[i]:
                    cnt+=1
                    continue
                break

        if chk ==0:
            for i in range(cnt):
                b[i] += steps[1][2]
            chk += b[0]
            prev = b[0]
        else:
            chk += steps[1][2]

        b = b[cnt:]
        if steps[1][2] >= b[0]:
            first = b[0]
            b = [b[i]-first for i in range(len(b)) ]
        else:
            b = [b[i] - prev for i in range(len(b))]

    while True:  # b
        ## 최대3명까지 같이
        if chk == 0:
            cnt = a.count(a[0])
            if cnt > 3:
                cnt = 3
        else:
            cnt = 0
            for i in range(len(a)):
                if cnt == 3:
                    break
                if steps[1][2] > a[i]:
                    cnt += 1
                    continue
                break

        if chk == 0:
            for i in range(cnt):
                a[i] += steps[1][2]
            chk += a[0]
            prev = a[0]
        else:
            chk += steps[1][2]

        a = a[cnt:]
        if prev >= a[0]:
            first = a[0]
            a = [a[i] - first for i in range(len(a))]
        else:
            a = [a[i] - prev for i in range(len(a))]



def powerset(n,k):

    if n == k:
        cal()
        return
    else:
        A[k]=1  ## 계단에 따라서 0,1
        powerset(n,k+1)
        A[k] = 0
        powerset(n,k+1)
    pass

T = int(input())
for _ in range(1,T+1):
    N = int(input())
    mat = [list(map(int,input().split())) for i in range(N) ]
    datas=[]
    steps=[]
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                datas.append((i,j))
                continue
            if mat[i][j] > 1:
                steps.append((i,j,mat[i][j]))

    A = [0]*len(datas)
    powerset(len(datas),0)

