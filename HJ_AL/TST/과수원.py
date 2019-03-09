def c1(x,y):
    sum = 0
    for i in range(0,x):
        for j in range(0,y):
            if mat[i][j] == 1:
                sum+=1
    return sum

def c2(x, y):
    sum = 0
    for i in range(0, x):
        for j in range(y, size):
            if mat[i][j] == 1:
                sum += 1
    return sum

def c3(x, y):
    sum = 0
    for i in range(x, size):
        for j in range(0, y):
            if mat[i][j] == 1:
                sum += 1
    return sum

def c4(x, y):
    sum = 0
    for i in range(x, size):
        for j in range(y, size):
            if mat[i][j] == 1:
                sum += 1
    return sum


def cal(x,y):
    if c1(x,y) == c2(x,y) == c3(x,y) ==c4(x,y):
        return 1
    return 0

def main():
    global mat
    global size
    size = int(input())
    mat = [ list(map(int,input())) for i in range(size) ]
    # print(mat)
    if size == 1:
        print(-1)
        return
    result = 0
    for i in range(1,size):
        for j in range(1,size):
            result += cal(i,j)

    if result == 0:
        print(-1)
        return
    print(result)


if __name__ == "__main__":
    main()