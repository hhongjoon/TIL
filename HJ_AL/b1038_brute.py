prob = int(input())
count = 10
result = 10
if prob <= 10:
    print(prob)
else:
    while(prob != result):
        count+=1
        judge=True
        for i in range(0,len(str(count))-1):
            if int(str(count)[i])>int(str(count)[i+1]):
                continue
            else:
                judge=False
                break
        if judge == True:
            result+=1
    print(count)
