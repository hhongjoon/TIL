
def calpower(loc):
    tt = [ datas[i][:] for i in range(len(datas))]
    for i in loc:
        if tt[i][2]<=0:
            continue

        mx = tt[i][0]
        my = tt[i][1]

        for j in range(len(tt)):
            sx, sy, se = tt[j]
            if se<=0:
                continue
            global D, P
            tempD =  abs(mx-sx) + abs(my-sy)
            if D >= tempD:
                 tt[j][2] = se-P
    # 남아 있는 것 카운트
    cnt = 0
    for i in tt:
        if i[2] >0:
            cnt+=1

    return cnt


def perm(n,k,loc):
    if n == k:
        print(loc)
        cnt = calpower(loc)
        global mincnt
        if mincnt>cnt:
            mincnt = cnt

        return
    else:
        for i in range(len(datas)):
            temp = loc[:]
            perm(n,k+1, temp+[i])


N = int(input())
datas = []
for i in range(N):
    x,y,E = map(int,input().split())
    datas.append([x,y,E])

mis, P, D = map(int,input().split()) # 개수/ 화력/ 범위

mincnt = 9999
perm(mis,0,[])
print(mincnt)