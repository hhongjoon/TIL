def result(T):
    a = 0
    b = 0
    c = 0
    while T != 0:
        if T >= 300:
            T = T - 300
            a += 1
        elif T >= 60:
            T = T - 60
            b += 1
        elif T >= 10:
            T = T - 10
            c += 1
        else:
            print(-1)
            return

    print(a,b,c)

T = int(input())
result(T)