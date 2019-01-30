# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.


a, b = list(map(int, input().split()))
count = 0
for i in range(a,b+1):
    copyi = i
    while i>1:
        i -= 1
        if i == 1:
            print(copyi)
            break
        if copyi % (i) == 0:
            break

