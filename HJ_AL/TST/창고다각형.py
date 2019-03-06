def main():
    N = int(input())
    loc = [0]*1001

    for i in range(N):
        l, s = map(int, input().split())
        loc[l]=s

    # print(loc)
    maxsize = max(loc)

    # 맥스사이즈 개숫 및 위치
    locmax=[]
    for i in range(1,1001):
        if loc[i] == maxsize:
            locmax.append(i)

    # 맥스사이즈가 여러개일 때 구하기
    if len(locmax)>1:
        for i in range(min(locmax),max(locmax)):
            loc[i] = maxsize


    # 맥스사이즈 기준 왼쪽
    prevsize = 0
    for i in range(1,1001):
        if loc[i] == maxsize:
            break
        if loc[i] == 0 and prevsize==0:  # 진입 전
            continue
        if loc[i]>prevsize:        # 진입 했을 때 현재>이전
            prevsize = loc[i]
        else:
            loc[i]=prevsize


    ## 맥스사이즈 기준 오른쪽
    prevsize=0
    for i in range(1000,-1,-1):
        if loc[i] == maxsize:
            break
        if loc[i] == 0 and prevsize==0:  # 진입 전
            continue
        if loc[i]>prevsize:        # 진입 했을 때 현재>이전
            prevsize = loc[i]
        else:
            loc[i]=prevsize

    print(sum(loc))

if __name__ == "__main__":
    main()