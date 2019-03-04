def howtall(x,y):
    mintall = 9999
    ok=True
    for p in range(4): ## 네방향 숫자가 같을 때
        if mat[x + dx[p]][y + dy[p]] != mat[x][y]:
            ok = False
    if ok:            ## 상하좌우와 자기 값이 같다면  +1
        return 1

    for p in range(4): # 같지 않을 때
        if mat[x+dx[p]][y+dy[p]] < mat[x][y]:
            return 0
        # else:                                      # 어차피 시작이 0, 1 밖에 없고 자기 값에 1만 더하면 됨
        #     tall = mat[x+dx[p]][y+dy[p]]
        #     if tall < mintall:
        #         mintall = tall

    return 1

##시작
size = int(input())
mat=[ [0]*(size+2) for i in range(size+2)      ]

content=[]
for i in range(size):
    content.append(list(map(int,input())))


for i in range(1,size+1):
    for j in range(1,size+1):
        mat[i][j] = content[i-1][j-1]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

#계산부

while True:
    check = False    ## 변화가 있으면 중간에 True로 바뀜
    maxtall = 0
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if mat[i][j] != 0:
                height = howtall(i,j)
                mat[i][j] += height

                if height > 0:
                    check = True # 바뀌면 True

                if maxtall < mat[i][j]:  # 언덕 높이 최대값 찾기
                    maxtall = mat[i][j]

    if check == False: #안바꼈으면 브레잌
        break

print(maxtall)

