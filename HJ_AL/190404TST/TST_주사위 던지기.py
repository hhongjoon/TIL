# 중복순열 / 매 자리 모든 숫자 가능
def dfs1(n):
    if n == N:
        print(*dice)
        return
    for i in range(1, 7):
        dice[n] = i
        dfs1(n + 1)


# 중복조합 / 숫자 순서 상관 X / 첫자리 고정 시킨 후 뒤에만 돌림 / 주사위라 전부 다름
def dfs2(n, k):
    if n == N:
        print(*dice)
        return
    for i in range(k, 7):
        dice[n] = i
        dfs2(n + 1, i)


# 순열 / 앞에서 쓴 숫자를 사용하지 않음
def dfs3(n):
    if n == N:
        print(*dice)
        return
    for i in range(1, 7):
        if visit[i]: continue
        dice[n] = i
        visit[i] = 1
        dfs3(n + 1)
        visit[i] = 0


# 조합
def dfs4(n, k):
    if n == N:
        print(*dice)
        return
    for i in range(k, 7):
        dice[n] = i
        dfs4(n + 1, i + 1)


N, M = map(int, input().split())
visit = [0] * 7
dice = [0] * N

if M == 1:
    dfs1(0)
elif M == 2:
    dfs2(0, 1)
elif M == 3:
    dfs3(0)
elif M ==4:
    dfs4(0,1)