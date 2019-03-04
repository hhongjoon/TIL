T = int(input())
mat = [  [0]*100   for i in range(100)   ]

# for i in range(100):
#     print(mat[i])

for i in range(T):
    x, y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            mat[y+i][x+j] = 1


    # for i in range(100):
    #     print(mat[i])

sum = 0
for r in range(100):
    for c in range(100):
        if mat[r][c] == 1:
            sum+=1
print(sum)