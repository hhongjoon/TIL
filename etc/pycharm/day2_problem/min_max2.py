import sys
sys.stdin = open("minmax_input.txt")
case = int(input())

for i in range(case):
    num = int(input())
    nums = list(map(float, input().split()))
    max_num = -1
    min_num = 99999999999999999999999999
    for j in nums:
        if j >max_num:
            max_num = j
        if j < min_num:
            min_num = j
    print(f"#{i+1} {int(max_num - min_num)}")

