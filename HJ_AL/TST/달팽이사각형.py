size = int(input())
mat = [[0]*size for i in range(size) ]
# print(mat)
count = 1
dx = [0,1,0,-1]  # 오 아 왼 위
dy = [1,0,-1,0]
x,y = 0,-1       # 배열 바깥에서 들어온다
pivot = 0         # 미리 피봇을 정해놓고 가던 길을 우선으로 간다.

while count <= (size*size):          # 넣는 수가 배열크기보다 커지면 중단
    if x+dx[pivot] >=size or y+dy[pivot] >=size or x+dx[pivot]<0 or y+dy[pivot]<0: #인덱스 에러 감지
        if pivot == 3:
            pivot=-1
        pivot += 1
        continue

    if mat[x+dx[pivot]][y+dy[pivot]] != 0:       # 갈 수 있는 길인지 아닌지 감지
        if pivot == 3:
            pivot=-1
        pivot += 1
        continue

    mat[x+dx[pivot]][y+dy[pivot]] = count         # 해당 값 입력
    x,y = x+dx[pivot], y+dy[pivot]                # x,y 재설정
    # print(mat)
    count+=1

for i in range(size):
    for j in range(size):
        print(mat[i][j],end=" ")
    print()