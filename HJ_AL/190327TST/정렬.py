def quick(L):
    if len(L)<= 1:
        return L
    pivot= L[len(L)-1]
    less = []
    equal = []
    more = []
    for i in L:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            equal.append(i)

    return quick(less) + equal + quick(more)


N = int(input())
datas = list(map(int,input().split()))
# for i in range(N):
#     for j in range(i+1,N):
#         if datas[i] > datas[j]:
#             datas[i], datas[j] = datas[j],datas[i]
# for j in datas:
#     print(j, end=' ')
res = quick(datas)
for j in res:
    print(j, end=" ")
