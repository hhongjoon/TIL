N, kind, eats, c = map(int,input().split())
table = []
for i in range(N):
    table.append(int(input()))
table = table + table[:eats-1]
maxval = -1
for i in range(0,N):
    val = len(set(table[i:i+eats]+[c]))
    if val >maxval:
        maxval = val
print(maxval)
