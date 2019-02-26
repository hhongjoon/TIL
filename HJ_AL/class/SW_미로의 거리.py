# import sys
# sys.stdin = open("미로의 거리.txt")

def findresult(i,j,size,length):

    #print(i,j, length)
    if mat[i][j] == 3:
        global result
        result = length-1
        return length
    mat[i][j] = 1
    if i-1 > -1 and mat[i-1][j] != 1:
        findresult(i-1,j,size, length+1)

    if j+1 < size and mat[i][j+1] != 1:
        findresult(i,j+1, size, length+1)

    if i+1 < size  and mat[i+1][j] != 1:
        findresult(i+1,j, size, length+1)

    if j-1 > -1 and mat[i][j-1] != 1:
        findresult(i,j-1, size, length+1)


T = int(input())
for _ in range(T):
    size = int(input())
    mat=[]
    for i in range(size):

        mat.append(list(map(int,list(input()))))
    print(mat)


    for i in range(size):
        for j in range(size):
            if mat[i][j] == 2:
                start = (i,j)

    result=0
    findresult(start[0],start[1],size,0)
    print(f"#{_+1} {result}")