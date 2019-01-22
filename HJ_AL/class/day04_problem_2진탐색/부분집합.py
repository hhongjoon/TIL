import sys
sys.stdin = open("부분집합_input.txt")
arr = [1,2,3,4,5,6,7,8,9,10,11,12]

n = len(arr)


T = int(input())
for iii in range(T):
    ea, ans = map(int,input().split())
    #print(ea, ans)
    result = 0
    for i in range(1<<n):
        count = 0
        sum = 0

        for j in range(n+1):
            #print(i,j)
            if i & (1<<j):
                count += 1
                sum += arr[j]
                #print(arr[j], end=", ")
        if count == ea and ans == sum:
            result += 1

    print(f"#{iii+1} {result}")


