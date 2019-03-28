# def powerset(N,k,cnt):
#     if sum(cnt)>M:
#         return
#     if len(cnt) == 3:
#         if sum(cnt) ==M:
#             cnt.sort()
#             print(cnt)
#         return
#     if k==6:
#         return
#     else:
#         A[k]==1
#         powerset(N,k+1,cnt+[k+1])
#         A[k]==0
#         powerset(N,k+1,cnt)

def jusawi(chan,cnt):
    if sum(cnt)>M:
        return

    if chan == 0:
        if sum(cnt)==M:
            for i in cnt:
                print(i, end=" ")
            print()
        return

    for i in range(1,7):
        temp=cnt[:]
        jusawi(chan-1,temp+[i])

N, M = map(int,input().split())
jusawi(N,[])
