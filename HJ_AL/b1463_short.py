n = int(input())
dp = [0, 0, 1, 1]
if n>3 :
    for i in range(4, n+1) :
        check = [dp[i-1]]
        if i%2==0 :
            check.append(dp[i//2])
        if i%3==0 :
            check.append(dp[i//3])
        dp += [min(check) + 1]
print(dp[n])