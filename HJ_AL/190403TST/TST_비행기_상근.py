def dfs(y, x, curSum):
    print(y,x)
    global maximum
    if y == 0:
        maximum = max(maximum, curSum)
    else:
        for i in range(-1, 2):
            nx = x+i
            if 0<=nx< 5 and curSum+array[y-1]*10 > maximum:
                dfs(y-1, nx, curSum+bombgrid[y-1][nx])
T = int(input())
for tc in range(T):
    grid = [list(input()) for _ in range(13)]
    array = [0] * 13
    for y in range(13):
        for x in range(5):
            if grid[y][x] == '*':
                grid[y][x] = 10
                array[y] += 1;
                continue
            elif grid[y][x] == 'X':
                grid[y][x] = -7
                continue
            else:
                grid[y][x] = 0;
                continue;
    for i in range(1,13):
        array[i] += array[i-1]
    maximum = -99999
    bombgrid = [[0 for _ in range(5)] for _ in range(13)]
    for y in range(9):
        for i in range(13):
            for j in range(5):
                bombgrid[i][j] = grid[i][j]
        for k in range(5):
            for x in range(5):
                    bombgrid[y+k][x] = 0 if bombgrid[y+k][x] == -7 else bombgrid[y+k][x]
        dfs(12,2,0);
    print(maximum)