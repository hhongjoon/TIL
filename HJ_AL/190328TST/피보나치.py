def fiv(n):
    if n == 1 or n==2:
        return 1
    return fiv(n-1)+fiv(n-2)

# print(fiv(N))
N = int(input())

dp = [1,1]
st = 2
if N<=2:
    print(1)
else:
    while st<N:
        dp.append(dp[st-1]+dp[st-2])
        st+=1
    print(dp[-1])