# 양방향 순환 큐
size, ea = map(int,input().split())
idxs = list(map(int,input().split()))
datas = list(range(1,size+1))
# print(datas)

pivot = 0
cnt =0
while len(idxs)> 0:
    idx = idxs.pop(0)

    if idx == datas[pivot]:  # 자기 자리일 때는 연산 1
        datas.pop(pivot)
        if len(datas)<=pivot:  # 마지막이면 피봇을 다음 값 0 으로
            pivot = 0

    else:             ## 연산 2, 3
        loc = datas.index(idx)
        stp1 = abs(loc-pivot)
        stp2 = len(datas) - stp1
        cnt += min(stp1,stp2)  # 최소값 더해줌
        pivot = loc
        datas.pop(loc)
        if len(datas)<=pivot:        ## 마지막일 때 피봇을 다음 값으로 넘겨줌
            pivot = 0

    # print(idx,pivot,cnt,datas)
print(cnt)
