#사람이 가장 많을 때
data = []
for i in range(4):
    a, b = map(int,input().split())
    data.append([a,b])
maxsum = 0
base = 0
for i in range(4):
    base = data[i][1] - data[i][0] + base
    if base >= maxsum:
        maxsum = base
print(maxsum)