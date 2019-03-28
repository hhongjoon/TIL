
def cal(m):
    summ = 0
    for i in datas:
        if i>m:
            summ+= (i-m)
    return summ
def bound(s,e):

    while s<=e:
        m = (s+e)//2
        res = cal(m)
        if res>M:
            s=m+1
        elif M == res:
            return m
        else:
            e=m-1
    return s-1



N, M = map(int,input().split())
datas = list(map(int,input().split()))
e = max(datas)
s=0
print(bound(s,e))



