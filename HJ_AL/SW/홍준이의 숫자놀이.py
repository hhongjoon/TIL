T = int(input())
for _ in range(T):
    A, B = map(int,input().split())
    x=1
    while True:
        if (1-A*x)%B == 0:
            break
        else:
            x+=1
    y = (1-A*x)//B
    print("#{} {} {}".format(_+1,x,y))