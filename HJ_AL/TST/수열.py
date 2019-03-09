
N = int(input())
data = list( map(int,input().split()))

maxlen = -1
prevval = -1
result = 0
for i in range(len(data)):
    if data[i] >= prevval:
        prevval=data[i]
        result+=1
        if result > maxlen:
            maxlen = result
    else:
        result = 1
        prevval =data[i]


asd = maxlen
# print(asd)

maxlen = -1
prevval = 100
result = 0
for i in range(len(data)):
    if data[i] <= prevval:
        prevval=data[i]
        result+=1
        if result > maxlen:
            maxlen = result
    else:
        result = 1
        prevval =data[i]

dsd = maxlen
# print(dsd)

if asd>dsd:
    print(asd)
else:
    print(dsd)
