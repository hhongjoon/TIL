def DFS(r, c, cnt=1, k=True):
    global arr, Max, visited
    visited[r][c] = True
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N and 0 <= cc < N and [rr, cc] and not visited[rr][cc]:
            if arr[rr][cc] < arr[r][c]:
                DFS(rr, cc, cnt + 1, k)
            elif k:
                for kk in range(1, K + 1):
                    if arr[rr][cc] - kk == arr[r][c] - 1:
                        arr[rr][cc] -= kk
                        DFS(rr, cc, cnt + 1, False)
                        arr[rr][cc] += kk
                    else:
                        Max = max(Max, cnt)
            else:
                Max = max(Max, cnt)
    visited[r][c] = False


for test in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = []
    H = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
        H = max(H, max(temp))
    highest = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == H:
                highest.append([r, c])
    Max = 0
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    for rr, cc in highest:
        visited = [[False] * N for ___ in range(N)]
        DFS(rr, cc)
    print('#{} {}'.format(test, Max))