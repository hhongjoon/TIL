## 3^n 개 비교, 이런식으로 여러개로 쪼개서 재귀시킬수 있어야함 unk + a = b       나머지:c
"""
 추들의 무게와 확인할 구슬들의 무게가 입력되었을 때,
주어진 추만을 사용하여 구슬의 무게를 확인 할 수 있는지를 결정하는 프로그램을 작성하시오.

"""
def powerset(n,k,a,b,c):
    global flag
    if flag:
        return
    if unk + a == b:
        flag = True
        return

    if n == k:
        return
    else:
        plus = datas[k]
        powerset(n,k+1,a+plus,b,c)
        powerset(n,k+1,a,b+plus,c)
        powerset(n,k+1,a,b,c+plus)



N = int(input())
datas = list(map(int,input().split()))
unkN = int(input())
undatas = list(map(int,input().split()))

for unk in undatas:
    flag = False
    powerset(N,0,0,0,0)
    if flag:
        print('Y', end = " ")
    else:
        print('N', end=" ")