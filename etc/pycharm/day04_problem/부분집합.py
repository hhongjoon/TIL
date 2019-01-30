# #1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
#
# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
#
#
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.


import sys
sys.stdin = open("부분집합_input.txt")
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
#arr = {1,2,3}

n = len(arr)


T = int(input())
for iii in range(T):
    ea, ans = map(int,input().split())
    #print(ea, ans)
    result = 0
    for i in range(1<<n): # 전체 부분집합의 갯수 2의 n제곱 개개
        count = 0
        sum = 0

        for j in range(n+1): # 갯수만큼 탐색
            print(i,j)
            if i & (1<<j):  ## 겹치면 True, 숫자가 12개면 자릿수는 0~11 // 겹치는 자릿수를 구하는 것임. 3자리가 겹친다 => 부분집합의 갯수가 3개 / 이런식으로 생각
                count += 1
                sum += arr[j]
                #print(arr[j], end=", ")
        if count == ea and ans == sum:
            result += 1

    print(f"#{iii+1} {result}")


