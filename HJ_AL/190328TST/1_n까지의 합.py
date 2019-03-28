def summ(n):
    if n ==0:
        return 0
    return n+summ(n-1)

N = int(input())
print(summ(N))
