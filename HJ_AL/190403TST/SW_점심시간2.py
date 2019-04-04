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
    # print(a, 'a')
    # print(b, 'b')
    chk_a, chk_b =0,0


    if len(a)>0:
        if chk_a == 0:
            cnt = min(len(a),3)
            for i in range(cnt):
                a[i]+= steps[0][2]
        if len(a)<=3:
            chk_a = a[-1]
        else:
            for i in range(len(a)-3):
                if a[i+3]<=a[i]:
                    a[i+3] = a[i]+steps[0][2]
                else:
                    a[i + 3] = a[i] + steps[0][2] + (a[i+3]-a[i])
            chk_a = a[-1]
    ################# b
    if len(b)>0:
        if chk_b == 0:
            cnt = min(len(b), 3)
            for i in range(cnt):
                b[i] += steps[1][2]
        if len(b) <= 3:
            chk_b = b[-1]
        else:
            for i in range(len(b) - 3):
                if b[i+3]<=b[i]:
                    b[i+3] = b[i]+steps[1][2]
                else:
                    b[i + 3] = b[i] + steps[1][2] + (b[i+3]-b[i])
            chk_b = b[-1]

    # print(chk_a)
    # print(chk_b)
    return max(chk_a,chk_b)




def powerset(n,k):

    if n == k:
        res = cal()
        global minres
        if minres > res:
            minres = res
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

    minres = 99999999
    powerset(len(datas),0)
    print("#{} {}".format(_,minres))

