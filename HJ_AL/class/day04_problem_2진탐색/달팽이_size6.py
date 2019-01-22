def iswall(i,j):
    if i>=size or i < 0:
        return True
    if j>=size or j < 0:
        return True
    return False
def isfull(i,j):
    if arr_reset[i][j] > 0:
        return True
    return False

size = int(input('size를 입력하세요 : '))

arr_reset = [[0 for i in range(size)] for i in range(size)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
copy_arr = list(range(1,size*size+1))
pivot = 0  # 피봇
i = 0
j = -1
while len(copy_arr)>0:
    temp = copy_arr.pop(0)

    while True:
        test_di = i + di[pivot]
        test_dj = j + dj[pivot]
        if iswall(test_di, test_dj) or isfull(test_di, test_dj):
            if pivot == 3:
                pivot = 0
                continue
            pivot+=1
            continue

        break

    i = test_di
    j = test_dj
    arr_reset[i][j] = temp
    ###
    #print(arr_reset)


#print(arr_reset)

[print(i) for i in arr_reset]


print("\n".join(map(str, arr_reset)))