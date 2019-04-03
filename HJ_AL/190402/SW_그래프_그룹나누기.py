def findset(a):
    while groups[a] != a:
        a = groups[a]
    return a

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    groups =list(range(0,N+1))

    datas = list(map(int,input().split()))

    for i in range(0,len(datas),2):
        a = datas[i]
        b = datas[i+1]

        # if groups[a] == a:
        #     groups[b] = groups[a]
        # else:
        #     groups[b] = findset(a)

        groups[findset(b)] = findset(a) # 대입, 부모값도 대표값으로
        print(groups)

    cnt = 0

    # print(groups)
    for i in range(1, N + 1):  # 대표원소가 자기 자신인 경우의 수
        if groups[i] == i:
            cnt += 1
    print('#{} {}'.format(_+1, cnt))
