import sys
sys.stdin = open("종이붙이기.txt")

def fact(n):
    result = 1
    for i in range(n,0,-1):
        result *= i
    return result

T = int(input())

for _ in range(T):
    size = int(input())
    square = size//20


    if size%20 == 10:  # 홀수이 때
        bar = 1
        sum = 0
        for i in range(square,-1,-1):
            sum += (fact(i+bar)/(fact(i)*fact(bar)))*(2**i)
            bar +=2
        print(f"#{_+1} {int(sum)}")
    else:
        bar = 0
        sum = 0
        for i in range(square,-1,-1):
            sum += (fact(i + bar) / (fact(i) * fact(bar))) * (2 ** i)
            bar += 2
        print(f"#{_+1} {int(sum)}")
