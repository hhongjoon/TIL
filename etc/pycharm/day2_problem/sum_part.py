import sys
sys.stdin = open("sumpart_input.txt")


case = int(input())
for k in range(case):
    a, b = map(int,input().split())
    nums = list(map(int,input().split()))
    max_sum = -1
    min_sum = 999999999999
    for i in range(0, a-b+1):
        sum = 0
        for j in range(b):
            sum +=nums[i+j]
        if sum > max_sum:
            max_sum = sum
        if sum < min_sum:
            min_sum =sum
    print(f"#{k+1} {max_sum-min_sum}")