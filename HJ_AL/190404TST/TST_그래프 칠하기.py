
def findloc(n):

    for i in range(N):
        for j in range(0,i+1):
            if mat[i][j] == 1 and i==n :
                path[j]=1
            if mat[i][j] == 1 and j==n :
                path[i]=1



'''
M개의 색으로 N개의 노드를 칠 할 수 있는지
'''
N, M = map(int,input().split())
mat = [ list(map(int,input().split())) for i in range(N) ]
# print(mat)

visited = [-1]*N
for i in range(N):
    flag = False
    colors = [False] * M
    path = [0] * N
    findloc(i)
    for j in range(len(path)):  # 경로들 주변에 칠해있는 색 다 구함  0 주변에 연결된 노드들 중 사용된 색 구함
        if path[j] == 1:
            if visited[j] == -1:
                continue
            colors[visited[j]]=True
    for j in range(len(colors)):  # 색들을 돌리면서 있으면 continue 없으면 해당 노드에 배정
        if colors[j] == True:
            continue
        flag=True
        visited[i] = j
        break

if flag == False:      # 배정되지 못한다면 -1 출력
    print(-1)
else:
    for i in visited:
        print(i+1, end=" ")

