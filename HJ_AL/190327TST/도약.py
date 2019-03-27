
def lowerSearch(s,e,data):
    sol = -1
    while s<=e:
        m = (s+e)//2
        # print(s,e)
        if datas[m]>=data:      # 데이터 이상이면 왼쪽 영역 재탐색
            sol = m
            e = m-1
        else: s= m+1
    return sol

def upperSearch(s,e,data):
    sol = -1
    while s<= e:
        m  = (s + e) //2
        if datas[m] <= data:     ## 데이터 이하면 오른쪽 재탐색
            sol = m
            s = m+1
        else:
            e = m-1
    return sol
#===========================================
N = int(input())
datas=[]
for i in range(N):
    datas.append(int(input()))
datas.sort()
cnt = 0
for i in range(len(datas)-2):
    for j in range(i+1,len(datas)-1):
        start = datas[j] + (datas[j] - datas[i])
        end = datas[j] + (datas[j] - datas[i])*2
        lo = lowerSearch(j+1,N-1,start)
        if lo == -1 or datas[lo]>end: continue
        up = upperSearch(j+1, N-1, end)
        cnt += (up-lo+1)
print(cnt)