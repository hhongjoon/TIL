def iswall(x,y):
    if x >-1 and y>-1 and x<len(path) and y<len(path):
        return False
    return True

def hunt(a,b):
    # print(a,b)

    global count
    for i in range(8):
        x,y = a,b
        while True:
            if iswall(x+dx[i], y+dy[i]) or path[x+dx[i]][y+dy[i]] == 1 or path[x+dx[i]][y+dy[i]] ==0:
                break

            if path[x + dx[i]][y + dy[i]] == 2:
                count+=1
                path[x + dx[i]][y + dy[i]] = 3
                x += dx[i]
                y += dy[i]
            else:  # 3일 경우
                x += dx[i]
                y += dy[i]
                continue



size = int(input())
path = []
for i in range(size):
    path.append(list(map(int,input())))

# print(path)
dx = [0, 1, 0, -1, -1, 1, 1 , -1]
dy = [1, 0, -1, 0,  1, 1, -1, -1]

# 사냥꾼위치
hunters=[]
for i in range(size):
    for j in range(size):
        if path[i][j] == 1:
            hunters.append((i,j))
#탐색, 사냥꾼별로
count = 0
for i in hunters:
    hunt(i[0],i[1])
    # print(count)

print(count)