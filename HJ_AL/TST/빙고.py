def marking(num):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == num:
                mat[i][j] = 'X'
                return

def check_bing():
    #가로
    sum=0
    for i in range(5):
        check=True
        for j in range(5):
            if mat[i][j] != 'X':
                check = False
                break
        if check == True:
            sum+=1
    #세로
    for i in range(5):
        check=True
        for j in range(5):
            if mat[j][i] != 'X':
                check = False
                break
        if check == True:
            sum+=1
    #대각 왼위
    check=True
    for i in range(5):
        if mat[i][i] != 'X':
            check=False
    if check ==True:
        sum+=1

    #대각 오른위
    check = True
    for i in range(5):
        if mat[i][4-i] != 'X':
            check = False
    if check == True:
        sum += 1

    return sum



mat = [0]*5
for i in range(5):
    mat[i] = list(map(int,input().split()))
# print(mat)

order = []
for i in range(5):
    order += list(map(int,input().split()))
# print(order)

for i in range(11):  # 최소 11개 까지 검사 / 12개부터 빙고 가능
    num = order.pop(0)
    marking(num)

for i in range(14):
    num = order.pop(0)
    marking(num)
    result = check_bing()
    if result >=3 :
        print(11+i+1)
        break