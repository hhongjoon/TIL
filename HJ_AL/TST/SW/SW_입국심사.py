def cal(mid,M):  # mid 초에 몇몇 가능한지
    temp = 0
    for i in chos:
        temp += mid//i   # 다 더함
    # print(temp)
    if temp >= M:
        return True
    else:
        return False


T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    chos=[]
    for i in range(N):
        chos.append(int(input()))
    left = 1
    right=10000000000000

    while left<=right:
        mid = left + (right-left)//2

        if left == right:
            break
        # print(left,mid,right)
        result = cal(mid,M)
        if result:
            right = mid-1
        else:
            left = mid+1



    print("#{} {}".format(_+1,mid))









