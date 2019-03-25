def recselection(B,s,e):
    # s = e 일 때 멈춘다
    mini = s
    if s== e: return
    for j in range(s+1,e,1):
        if B[j] < B[mini]:
            mini = j
    # swap
    B[s], B[mini] = B[mini], B[s]

    recselection(B,s+1,e)
#=====================================
def perm(n,k):
    if n == k:
        myprint(n)
    else:
        for i in range(k, n)
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            for i in range(k,n):


#=====================================
def babyjin:
    pass

#=====================================
N=3
A = [0 for _ in range(N)]

def powerset(n,k):
    if n ==k:
        return
    else:
        A[k] = 1
        powerset(n,k+1)
        A[k] = 0
        powerset(n,k+1)
#====================================
N=10
A = [0]*11
data = list(range(0,11))


def powerset(n,k,c):
    if c == 10:
        return
    else:
        A[k]=1

        powerset(n,k+1,c+data[k])
        A[k]=0
        powerset(n,k+1,c)













