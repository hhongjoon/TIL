def iswall(i,j):
    if i>=len(arr) or i < 0:
        return True
    if j>=len(arr) or j < 0:
        return True
    return False
def isfull(i,j):
    if arr_reset[i][j] > 0:
        return True
    return False

arr = [[9,20,2,18,11],
       [19,1,25,3,21],
       [8,24,10,17,7],
       [15,4,16,5,6],
       [12,13,22,23,14]
]

arr_reset = [[0 for i in range(len(arr))] for i in range(len(arr))]
copy_arr = []
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for aaa in range(len(arr)):
    copy_arr.extend(arr[aaa])

copy_arr.sort()

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
    print(arr_reset)
print(arr_reset)

[print(i) for i in arr_reset]


print("\n".join(map(str, arr_reset)))