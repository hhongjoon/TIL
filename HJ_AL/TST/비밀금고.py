T = int(input())
data = list(map(int,input().split()))
mat = [ [0]*T for i in range(T) ]
# print(mat)

for i in range(T):
    loc = 0
    j = i
    while True:
        mat[j][loc] = data.pop(0)

        if loc >= i:
            break
        loc +=1
        j-=1
# for i in range(T):
#     print(mat[i])
# print()

for i in range(T-1,0,-1):   # T=3
    loc = T-1
    j = i
    while True:
        mat[j][loc] = data.pop()

        if loc <= i:
            break
        loc -=1
        j+=1
# for i in range(T):
#    print(mat[i])

maxsum = -1
for i in range(T):
    j=0
    sum=0
    while i <= T-1 and j<=T-1:
        sum += mat[i][j]
        i+=1
        j+=1
    # print(sum)
    if sum >= maxsum:
        maxsum = sum

for i in range(T-1,0,-1):
    j=0
    sum=0
    while i <= T-1 and j<=T-1:
        sum += mat[j][i]
        i+=1
        j+=1
    # print(sum)
    if sum >= maxsum:
        maxsum = sum
print(maxsum)