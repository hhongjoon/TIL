x ,y = map(int,input().split())

mat = [   list(map(int,input().split()))       for i in range(x)     ]

for i in range(x):
    for j in range(y):
        if j-1 > -1 and mat[i][j-1] != 0:
            if mat[i][j] == 0:
                continue
            else:
                mat[i][j] += mat[i][j-1]

for i in range(x):
    for j in range(y):
        print(mat[i][j], end =" ")
    print()