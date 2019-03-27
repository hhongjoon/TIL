
def cal(dis):
    global mindis
    if dis>=B:
        if mindis > dis:
            mindis = dis
        return
def perm(N,k,dis):
    if mindis<dis:
        return
    if N == k:
        cal(dis)
    else:
        A[k]=1
        perm(N,k+1,dis+datas[k])
        A[k]=0
        perm(N,k+1,dis)

T = int(input())
for _ in range(T):
    N, B = map(int,input().split())
    datas = list(map(int,input().split()))
    mindis = 999999
    A = [0]*N
    perm(N,0,0)
    print("#{} {}".format(_+1,mindis-B))


# def calc(n, k, cursum):
#     global ans
#     if cursum >= B:
#         if ans > cursum:
#             ans = cursum
#         return
#
#
# def powerset(n, k, cursum):
#     if ans < cursum: return  # 가지치기
#
#     if n == k:
#         calc(n, k, cursum)
#     else:
#         A[k] = 1
#         powerset(n, k + 1, cursum + h[k])
#         A[k] = 0
#         powerset(n, k + 1, cursum)
#
#
# T = int(input())
# for tc in range(T):
#     N, B = map(int, input().split())  # 점원수, 선반
#     h = list(map(int, input().split()))  # 점원의 키들
#     A = [0] * N  # h가 있으므로 사용 안 함
#     ans = 0xfffffff
#     powerset(N, 0, 0)
#
#     print("#{} {}".format(tc + 1, ans - B))