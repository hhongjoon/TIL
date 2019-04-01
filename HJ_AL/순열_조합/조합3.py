def comb(n, r):
    memo = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, r)+1):
            if j == 0 or j == i:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
    return memo[n][r]

print(comb(52, 5))