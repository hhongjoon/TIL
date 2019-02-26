import sys
sys.stdin = open("회전.txt")

T = int(input())
for _ in range(T):
    ea, nums = map(int,input().split())
    input_nums=list(map(int, input().split()))
    #print (input_nums)
    pivot = nums % ea
    print(f"#{_+1} {input_nums[pivot]}")