def myprint(r):
    global tempsum, minsum
    minsum = sum(temp)
    # print(minsum, temp)
def p(n,r):
    if r == 0:
        print(temp)
        return
    for i in range(0,size):
        if visited[i] == True:
            continue
        else:
            temp[r-1] = data[i][r-1]
            # print(temp)
            visited[i] = True
            p(n-1,r-1)
            visited[i] = False






T = int(input())
for _ in range(T):
    global size
    size = int(input())
    data = [  list(map(int,input().split()))  for i in range(size)  ]
    # print(data)
    temp = [0]*size

    minsum = 9999999
    tempsum = 0
    visited = [False,False,False]
    p(size,size)
    print("#{} {}".format(_+1,minsum))