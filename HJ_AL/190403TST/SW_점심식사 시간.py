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
    print(a, 'a')
    print(b, 'b')
    # a
    if len(a) > 0:
        first = a[0]
    else:
        first=0
    chk_a = first
    while len(a)>0:
        cnt = 0
        first = a[0]

        if chk_a == first:
            for i in range(len(a)):
                if cnt == 3:
                    break
                if a[i] == first:
                    cnt+=1
                    continue
                break
        else:
            for i in range(len(a)):
                if cnt == 3:
                    break
                if a[i] <= chk_a:
                    cnt+=1
                    continue
                break
        if cnt == 0:
            chk_a += (steps[0][2] + a[0]-chk_a)
            a=a[1:]
            continue

        chk_a+=steps[0][2]
        a = a[cnt:]


    # b
    if len(b) > 0:
        first = b[0]
    else:
        first=0
    chk_b = first
    while len(b)>0:
        cnt = 0
        first = b[0]

        if chk_b == first:
            for i in range(len(b)):
                if cnt == 3:
                    break
                if b[i] == first:
                    cnt+=1
                    continue
                break
        else:
            for i in range(len(b)):
                if cnt == 3:
                    break
                if b[i] <= chk_b:
                    cnt+=1
                    continue
                break
        if cnt == 0:
            chk_b += (steps[1][2] + b[0]-chk_b)
            b=b[1:]
            continue
        chk_b+=steps[1][2]
        b = b[cnt:]



    print(chk_a, steps[0][2])
    print(chk_b, steps[1][2])
    return max(chk_a,chk_b)




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

