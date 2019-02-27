import sys
sys.stdin = open("숫자근.txt")

def solve(num):
    num = str(num)
    while True:
        sum = 0
        for i in num:
            sum += int(i)

        if sum >= 10:
            num = str(sum)
        else:
            break

    return sum

maxval = -1
T = int(input())
for _ in range(T):
    num = int(input())

    val = solve(num)
    #print(num, val)

    if val >= maxval:
        maxval = val
        if val == maxval:
            if minnum >num:
                minnum = num
            continue

        minnum = num


print(minnum)