t = int(input())


def check(L, time, num):
    count = 0
    for i in range(len(L)):
        count += time // L[i]
    print(count)
    return count >= num


for testcase in range(1, t + 1):
    n, m = map(int, input().split())
    L = [int(input()) for _ in range(n)]
    left = 1
    right = 1000000000000000000
    ans = 1000000000000000000
    while left <= right:
        mid = left + int((right - left) / 2)
        print(left, mid, right)
        if check(L, mid, m):
            if ans > mid:
                ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print('#{} {}'.format(testcase, ans))