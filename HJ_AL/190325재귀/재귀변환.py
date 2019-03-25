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

def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        min = i
