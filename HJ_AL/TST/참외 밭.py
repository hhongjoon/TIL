apple = int(input())
data = []
for i in range(6):
    dir , size = map(int,input().split())
    data.append(size)

maxval = max(data)
idx = data.index(maxval) + 6
data = data[:]+data[:]+data[:]
# print(data)

path =1
if data[idx+1] > data[idx-1]:
    big = data[idx+1]
    path = -1    # 역방향 / 이따가 곱해줄 것임
else:
    big = data[idx-1]

bigarea = big*maxval
if path == 1:
    smallarea = data[idx+2] * data[idx+3]
else:
    smallarea = data[idx-2] * data[idx-3]

print((bigarea-smallarea)*apple)