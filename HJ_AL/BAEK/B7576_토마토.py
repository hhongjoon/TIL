def iswall(x,y):
    if x>-1 and y>-1 and x<row and y<col:
        return True
    return False

def cal_days(start):
    cnt = 0
    new_start = start
    while True:
        temp = new_start
        new_start = []

        for i in temp:

            x = i[0]
            y = i[1]
            for j in range(4):
                nx = x+dx[j]
                ny = y+dy[j]
                if iswall(nx,ny) and mat[nx][ny] == 0:
                    new_start.append((nx,ny))
                    mat[nx][ny] = 1
        cnt +=1
        if len(new_start) == 0:
            return cnt-1



def main():
    global col,row
    col, row = map(int,input().split())
    global mat
    mat = [  list(map(int,input().split()))  for i in range(row)]
    # print(mat)
    flag = False
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 0:
                flag = True

    if flag == False:
        print(0)
        return

    start=[]
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1:
                start.append((i,j))
    global dx
    global dy
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    result = cal_days(start)
    # print(result)
    # 다 익었는지, 처음부터 다익어있는지
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 0:
                print(-1)
                return
    print(result)

if __name__ == "__main__":
    main()