def main():
    N = int(input())
    mat = [ [1]*(N+2) for i in range(N+2)  ]
    road = [  list(map(int,input()))    for i in range(N) ]
    for i in range(1,N+1):
        for j in range(1,N+1):
            mat[i][j] = road[i-1][j-1]
    # print(mat)
    order = list(map(int,input().split()))
    pivot = 0
    dx=[1, 0, -1, 0]
    dy=[0, -1, 0, 1]
    x,y=1,1
    count = 0
    while True:
        i = order[pivot]-1
        if mat[x+dx[i]][y+dy[i]] == 0:
            mat[x][y] = 2
            count+=1
            x = x + dx[i]
            y = y + dy[i]

            continue
        if mat[x+dx[i]][y+dy[i]] == 2:
            break

        if mat[x+dx[i]][y+dy[i]] == 1:
            if pivot ==3:
                pivot = 0
            else:
                pivot+=1

    print(count)

if __name__ == "__main__":
    main()