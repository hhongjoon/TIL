def make90(mat,size):
    mat90 = [ [0]*size for i in range(size) ]
    for i in range(size):
        for j in range(size):
            mat90[i][j] = mat[(size-1)-j][i]

    return mat90

def newprint(mat,size):
    for i in range(size):
        for j in range(size):
            print(mat[i][j],end=" ")
        # if i ==size-1:
        #     return
        print()

def main():
    size = int(input())
    base=[0]*size
    for i in range(size):
        base[i] = list(map(int,input().split()))
    # print(mat)
    while True:
        temp = int(input())
        if temp == 90:
            base = make90(base,size)
            newprint(base,size)
        elif temp == 180:
            base = make90(base,size)
            base = make90(base,size)
            newprint(base,size)

        elif temp == 270:
            base = make90(base, size)
            base = make90(base, size)
            base = make90(base,size)
            newprint(base, size)
        elif temp ==360:
            newprint(base,size)

        else:
            break




if __name__ == "__main__":
    main()