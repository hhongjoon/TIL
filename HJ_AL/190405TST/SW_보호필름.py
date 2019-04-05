

def cal():
    global K
    tempmat = [ mat[i][:]  for i in range(X) ]
    for i in range(len(A)):
        if A[i] == 0:
            continue
        elif A[i] ==1:  # A
            for j in range(Y):
                tempmat[i][j] = 0
        else:  # B
            for j in range(Y):
                tempmat[i][j] = 1

    return check(K,tempmat)

def powerset(n,k,cnt):
    global mincnt

    if mincnt<cnt:
        return

    if n ==k:
        # print(A)
        if cal():
            mincnt = min(mincnt,cnt)

        return
    else:
        for i in range(3):
            A[k] = i
            if i == 0:
                powerset(n,k+1,cnt)
            else:
                powerset(n,k+1,cnt+1)



def check(n,matt):
    for j in range(Y):
        for i in range(0,X-n+1):
            chk = matt[i][j]
            flag = True
            for k in range(n):
                if chk != matt[i+k][j]:
                    flag = False
                    break

            if flag:
                break

        if not flag:
            return False

    return True



T = int(input())
for _ in range(1,T+1):
    X,Y,K = map(int,input().split())
    mat = [ list(map(int,input().split())) for i in range(X) ]
    A = [0]*X
    mincnt = 999999
    powerset(X,0,0)
    print("#{} {}".format(_,mincnt))