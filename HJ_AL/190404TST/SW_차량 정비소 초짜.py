for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = list(map(int, input().split()))
    aq = [None] * N
    bq = [None] * M
    wait = []
    s, n, cnt = 0, 0, 0
    take = True
    while take or n < K:
        take = False
        for i in range(N):
            if aq[i]:
                take = True
                aq[i][0] -= 1
                if aq[i][0] == 0:
                    wait.append([aq[i][1], aq[i][2]])
                    aq[i] = None
            if not aq[i]:
                if n < K:
                    if t[n] <= s:
                        aq[i] = [a[i], i + 1, n + 1]
                        n += 1
        for j in range(M):
            if bq[j]:
                take = True
                bq[j] -= 1
                if bq[j] == 0:
                    bq[j] = None
            if not bq[j]:
                if wait:
                    temp = wait.pop(0)
                    bq[j] = b[j]
                    if temp[0] == A and j + 1 == B:
                        cnt += temp[1]
        s += 1

    if not cnt:
        cnt = -1
    print('#{} {}'.format(tc, cnt))