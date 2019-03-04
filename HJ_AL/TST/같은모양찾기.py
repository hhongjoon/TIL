def isok(x,y,findsize):
    for i in range(x, x+findsize):
        for j in range(y, y+findsize):
            if mat[i][j] != findmat[i-x][j-y]:
                return False
    return True

matsize = int(input())
mat = []
for i in range(matsize):
    mat.append(list(map(int,input())))
# print(mat)
findsize = int(input())
findmat = []
for i in range(findsize):
    findmat.append(list(map(int,input())))

#계산부
sum = 0
for i in range(0,matsize-findsize+1):
    for j in range(0,matsize-findsize+1):
        if isok(i,j,findsize):
            sum+=1

print(sum)
