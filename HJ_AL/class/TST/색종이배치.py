

def main():
    mat = [ [0 for j in range(102)] for i in range(102)  ]

    x, y, sizex, sizey = map(int,input().split())  # 1번입력
    for i in range(x,x+sizex):
        for j in range(y,y+sizey):
            mat[i][j]=1

    for i in range(x-1,x+sizex+1):
        mat[i][y-1] = 2
    for i in range(x-1,x+sizex+1):
        mat[i][y+sizey] = 2
    for j in range(y-1,y+sizey+1):
        mat[x-1][j] = 2
    for j in range(y-1,y+sizey+1):
        mat[x+sizex][j] = 2

    for i in range(len(mat)):
        print(mat[i])

    x2, y2, sizex2, sizey2 = map(int, input().split())  # 2번입력
    count = 0
    result = 0
    for i in range(x2, x2 + sizex2):
        for j in range(y2, y2 + sizey2):
            if mat[i][j] == 2:
                count+=1
    if count == 1:
        pass
























if __name__ == "__main__":
    main()