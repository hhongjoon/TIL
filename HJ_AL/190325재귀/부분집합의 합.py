N = 10
A = [0] * 10
data = list(range(1, 11))

def printset(c):
    # print(A,c)
    if c == 10:
        for i in range(0,10):
            if A[i] == 1:
                print(data[i], end=" ")
        print()


def powerset(n, k, c):
    if c>10:
        return
    global cnt
    cnt +=1


    if n== k:
        printset(c)

    else:
        A[k] = 1
        powerset(n, k + 1, c + data[k])
        A[k] = 0
        powerset(n, k + 1, c)

cnt = 0
print(A)
print(data)
powerset(10,0,0)
print(cnt,'회')