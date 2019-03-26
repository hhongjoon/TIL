
def comp(A,B):
    for i in range(len(A)):
        if A[i] == 'B' and B[i] == 'B':
            continue

        if A[i] in hole and B[i] in hole:
            continue
        if A[i] in etc and B[i] in etc:
            continue
        return 'DIFF'
    return 'SAME'

T = int(input())
for _ in range(T):
    A, B = map(str,input().split())
    if len(A) != len(B):
        print('#{} DIFF'.format(_+1))
        continue
    hole = ['A','D','O','P','Q','R']
    etc=['C','E','F','G','H','I','J','K','L','M','N','S','T','U','V','W','X','Y','Z']
    res = comp(A,B)
    print('#{} {}'.format(_ + 1, res))