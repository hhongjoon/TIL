def goant():
    global falls
    while len(locs)>0:
        for i in range(len(locs)):
            if go[i] >0 :
                locs[i] += 1
            else:
                locs[i] -= 1

        for i in range(len(locs)):
            for j in range(i+1,len(locs)):
                if locs[i] == locs[j]:
                    go[i] *= -1
                    go[j] *= -1
                if abs(locs[i] - locs[j]) <=1 and go[i]*go[j] == -1:
                    go[i] *= -1
                    go[j] *= -1


        temp=[]
        temp_idx=[]
        for i in range(len(locs)):
            if locs[i] > L or locs[i] <0:
                temp.append(ids[i])
                temp_idx.append(i)

        for i in temp_idx:
            del ids[i]
            del locs[i]
        temp.sort()
        falls += temp
        if len(falls)>=k:
            return falls[k-1]



T = int(input())
for _ in range(T):
    global N, k
    N, L, k = map(int,input().split())
    locs = []
    ids = []
    go = []
    falls = []

    for i in range(N):
        loc, id = map(int,input().split())
        locs.append(loc)
        ids.append(id)
        if id<0:
            go.append(-1)
        else:
            go.append(1)

    print(goant())
