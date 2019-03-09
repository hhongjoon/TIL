def check(a,b):
    check={}
    for i in a:
        if check.get(i) is None:
            check[i] = -1
        else:
            return 0 # 중복이니까 실패

    for j in b:
        if check.get(j) is None:
            check[j] = 0  # 두번째 회사 들어오는 것
        else:
            check[j] += 1
            if check[j] >= 1:
                return 0
    if len(a)+len(b) - len(check) >= 2:  # 갯수가 없다면 중복이 많다는 것
        return 0
    return 1


T = int(input())
sum = 0
for i in range(T):
    L, H = input().split()
    sum += check(L,H)
print(T-sum)  ## 불량률 구해야지