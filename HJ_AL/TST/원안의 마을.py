def cal(i,j):
    d=1
    while d<=13:  #R 줄여가면서 출력
        if d**2 >= (i-locx)**2 + (j-locy)**2 : #안에 있다면
            return d
        d+=1
    return 13


size = int(input())
mat = [ list(map(int,input()))  for i in range(size)]
# print(mat)
# 기지국 찾기
for i in range(size):
    for j in range(size):
        if mat[i][j] == 2:
            locx = i
            locy = j
            break

maxR = -1
for i in range(size):
    for j in range(size):
        if mat[i][j] == 1:
            R = cal(i,j)
            if R >= maxR:
                maxR = R
print(maxR)
