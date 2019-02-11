import sys
sys.stdin = open("ladder.txt")
for _ in range(10):
    a = input()

    data = [ [] for a in range(100)]
    for i in range(100):
        data[i] = list(map(int,input().split()))

    goal = data[99].index(2)
    count = 99
    x = 99
    y= goal
    while True:
        #print(x,y)
        if x == 0:
            print(f"#{_+1} {y}")
            break

        if y+1 != 100 and data[x][y+1] == 1:  # 오른쪽
            data[x][y] = 9
            y=y+1
            continue
        if y-1 != -1 and data[x][y-1] == 1:   # 왼쪽
            data[x][y] = 9
            y=y-1
            continue
        if data[x-1][y] == 1:     #위에
            x=x-1
            continue

