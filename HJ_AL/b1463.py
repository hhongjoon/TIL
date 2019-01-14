# 1463

def cal(n):
    dp = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 0
            continue
        if i == 2:
            dp[i] = 1
            continue
        if i%3 ==0 and i%2 ==0 :
            dp[i] = min([dp[i-1],dp[int(i/3)], dp[int(i/2)]])+1
        elif i%3 ==0 :
            dp[i] = min([dp[i - 1], dp[int(i / 3)]]) + 1
        elif i%2 ==0 :
            dp[i] = min([dp[i-1], dp[int(i/2)]])+1
        else:
            dp[i] = dp[i-1]+1
    return dp[-1]
n = int(input())
print(cal(n))