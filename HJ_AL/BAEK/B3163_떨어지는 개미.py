def goant():
    while True:
        for i in range(len(data)-1):   #  부호변환
            if data[i+1][0] - data[i][0] <= 1 and go[i] >0 and go[i+1]<0:
                data[i+1],data[i] = data[i], data[i+1]
                go[i] *= -1
                go[i+1] *= -1
        for i in range(len(data)-1):  # 만났을 때 부호 변환
            if data[i][0] == data[i+1][0] :
                go[i]*= -1
                go[i+1] *= -1

        for i in range(len(data)):  # 이동
            if go[i]>0:
                data[i][0] += 1
            else:
                data[i][0] += -1
        temp = []
        for i in range(len(data)-1, -1, -1):
            if data[i][0] < 0 or data[i][0] >L:
                temp.append(data[i][1])
                del data[i]
        temp.sort()
        global falls
        falls += temp
        if len(falls)>k:
            return falls[k-1]



T = int(input())
for _ in range(T):
    global N, L, k
    N, L, k = map(int,input().split())
    data = []
    go = []
    falls=[]
    for i in range(N):
        loc, id = map(int,input().split())
        data.append([loc,id])
        if id < 0:
            go.append(-1)
        else:
            go.append(1)
    # print(data)
    # data.sort(key=lambda aaa:aaa[0], reverse=True)
    print(goant())
