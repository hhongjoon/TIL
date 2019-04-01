def check(dx, dy, l, r):
    global max_num
    po = []
    a, b = dx, dy
    for _ in range(l):
        a += 1
        b -= 1
        if X[a][b] not in po:
            po.append(X[a][b])
        else:
            return
    for _ in range(r):
        a += 1
        b += 1
        if X[a][b] not in po:
            po.append(X[a][b])
        else:
            return
    for _ in range(l):
        a -= 1
        b += 1
        if X[a][b] not in po:
            po.append(X[a][b])
        else:
            return
    for _ in range(r):
        a -= 1
        b -= 1
        if X[a][b] not in po:
            po.append(X[a][b])
        else:
            return
    if len(po) > max_num:
        max_num = len(po)


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    X = []

    for _ in range(N):
        X.append(list(map(int, input().split())))
    max_num = 0
    for i in range(N - 2):
        for j in range(1, N - 1):
            l, r, h = j - 0, N - 1 - j, N - 1 - i
            for x in range(1, l + 1):
                for y in range(1, r + 1):
                    if x + y <= h:
                        check(i, j, x, y)
    if not max_num:
        max_num = -1

    print('#{} {}'.format(t, max_num))