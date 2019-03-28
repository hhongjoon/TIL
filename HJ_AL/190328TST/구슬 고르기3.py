# def perm(n,k):
#     if n == k:
#         for i in A:
#             print(i, end=" ")
#         print()
#         return
#     else:
#         for i in range(k,n):
#             A[i], A[k] = A[k], A[i]
#             perm(n,k+1)
#             A[i], A[k] = A[k], A[i]


# perm(3,0)


def recdfs(v):
    if v == 3:
        for i in result:
            print(i,end=" ")
        print()
    else:
        for i in range(3):
            if visited[i] == 0:
                visited[i] = 1
                result[v] = A[i]
                recdfs(v+1)
                visited[i] = 0


A=[1,2,3]
visited=[0]*3
result=[0]*3
recdfs(0)