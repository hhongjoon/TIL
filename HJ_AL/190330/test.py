def fib(n, sum):
    if n < 1:
        return sum
    else:
        return fib(n-1, sum+n)

c = 998
print(fib(c, 0))