
def powerset(n,k,cnt, val,arr):
    global C, maxval
    if cnt >C:
        return
    if maxval < val:
        maxval = val

    if n==k:
        return
    else:
        plus = arr[k]**2
        powerset(n,k+1,cnt+arr[k],val+plus,arr)
        powerset(n,k+1,cnt,val,arr)


T = int(input())
for _ in range(1,T+1):
    N, M, C = map(int,input().split())
    mat = [ list(map(int,input().split())) for i in range(N) ]
    maxgoal = -1
    for x1 in range(N):
        for y1 in range(0,N-M+1):
            for x2 in range(N):
                for y2 in range(0,N-M+1):
                    if x1 == x2 and y1  > y2 -M:
                        continue
                    maxval = -1
                    A = mat[x1][y1:y1+M]
                    powerset(M,0,0,0,A)
                    resA = maxval
                    maxval = -1
                    B = mat[x2][y2:y2+M]
                    powerset(M, 0, 0, 0, B)
                    resB = maxval
                    if resA+resB > maxgoal:
                        maxgoal = resA+resB

    print("#{} {}".format(_,maxgoal))
