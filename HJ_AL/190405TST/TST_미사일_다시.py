
def cal():
    tempdatas = [ datas[i][:] for i in range(N) ]
    for i in A:

        if tempdatas[i][2]<=0:
            continue
        mx = tempdatas[i][0]
        my = tempdatas[i][1]

        for j in range(len(tempdatas)):
            sx,sy,se = tempdatas[j]
            # if tempdatas[i][2] <= 0:
            #     continue
            if abs(mx-sx) + abs(my-sy) <=D:
                tempdatas[j][2] -= P
    cnt = 0
    for i in tempdatas:
        if i[2]>0:
            cnt+=1
    return cnt

def perm(n,k):
    if n==k:
        # print(A)
        global mincnt
        mincnt = min(mincnt,cal())
        return
    else:
        for i in range(N):
            A[k] = i
            perm(n,k+1)


N = int(input())
datas=[]
for i in range(N):
    x,y,E = map(int,input().split())
    datas.append([x,y,E])
M,P,D = map(int,input().split())
A = [0]*M
mincnt = 99999
perm(M,0)
print(mincnt)