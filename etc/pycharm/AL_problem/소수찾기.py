# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
T = int(input())

in_list = list(map(int, input().split()))
count = 0
for i in in_list:
    copyi = i
    while i>1:
        i -= 1
        if i == 1:
            count+=1
            break
        if copyi % (i) == 0:

            break


print(count)