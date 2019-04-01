def find(arr, M):
    global C
    max_q = 0
    for i in range(1, 2 ** M):
        s = 0
        q = 0
        for j in range(M):
            if i & (1 << j) != 0:
                s += arr[j]
                q += arr[j] ** 2
                if s > C:
                    q = 0
        if max_q < q:
            max_q = q
    return max_q


for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for _ in range(2):
        max_num = 0
        for i in range(N):
            for j in range(N - M + 1):
                if res == 0:
                    break
                if [0] * N in numbers:
                    break
                if res == find(numbers[i][j:j + M], M):
                    numbers[i] = [0] * N
                    break
            for j in range(N - M + 1):
                p = find(numbers[i][j:j + M], M)
                if max_num < p:
                    max_num = p
        res += max_num
    # print(f"#{tc} {res}")