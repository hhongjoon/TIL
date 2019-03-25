def myprint(r):
    global tempsum, minsum
    minsum = sum(temp)
    # print(minsum, temp)
def pi(n,r):
    print(n,r)
    print(data)
    if r==0:
        print(temp, sum(temp))
        if sum(temp) > minsum:
            return
        else:
            myprint(r)
            return
    for i in range(n-1,-1,-1):
        for j in range(n - r-1):
            data[(n-1) - j][n-1], data[i][n-1] = data[i][n-1], data[(n-1)-j][n-1]

        temp[r-1]=data[n-1][n-1]
        pi(n-1,r-1)
        for j in range(n - r-1):
            data[(n-1) - j][n-1], data[i][n-1] = data[i][n-1], data[(n-1)-j][n-1]




T = int(input())
for _ in range(T):
    global size
    size = int(input())
    data = [  list(map(int,input().split()))  for i in range(size)  ]
    # print(data)
    temp = [0]*size

    minsum = 9999999
    tempsum = 0
    pi(size,size)
    print("#{} {}".format(_+1,minsum))