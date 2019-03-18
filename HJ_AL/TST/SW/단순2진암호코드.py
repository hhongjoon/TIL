pattern=[
    [0,0,0,1,1,0,1],
    [0,0,1,1,0,0,1],
    [0,0,1,0,0,1,1],
    [0,1,1,1,1,0,1],
    [0,1,0,0,0,1,1],
    [0,1,1,0,0,0,1],
    [0,1,0,1,1,1,1],
    [0,1,1,1,0,1,1],
    [0,1,1,0,1,1,1],
    [0,0,0,1,0,1,1],
]


def findend():
    for i in range(x):
        for j in range(y - 1, -1, -1):
            if mat[i][j] == 1:
                end = (i, j)
                return end



T = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    mat = [ list(map(int,input())) for i in range(x)  ]
    code=[]
    temp=[]
    end = findend()
    for i in range(56):
        temp.append(mat[end[0]][end[1]-55+i])
        if len(temp) == 7:
            code.append(temp)
            temp=[]
    code10=[]
    for i in code:
        for j in range(10):
            if i == pattern[j]:
                code10.append(j)
                break
    # print(code10)
    # print(((code10[0] + code10[2] + code10[4] + code10[6])*3 +(code10[1]+code10[3]+code10[5])+code10[7]))
    if ((code10[0] + code10[2] + code10[4] + code10[6])*3 +(code10[1]+code10[3]+code10[5])+code10[7])%10 == 0:
        print("#{} {}".format(_+1,sum(code10)))
    else:
        print("#{} {}".format(_+1,0))