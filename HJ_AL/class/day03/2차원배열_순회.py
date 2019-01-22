# arr = [[0,1,2,3],
#        [4,5,6,7],
#        [8,9,10,11]
#     ]
# # i : 행의자표
# # j : 열의 좌표
#
# for i in range(len(arr)):               ## 행우선
#     for j in range(len(arr[i])):
#         print(arr[i][j], end =" ")
#     print()
# print()
#
# for j in range(len(arr[0])):               ## 열우선
#     for i in range(len(arr)):
#         print(arr[i][j], end =" ")
#     print()
# print()

# for i in range(len(arr)):   ## 지그재그
#     for j in range(len(arr[0])):
#         if i%2 == 0:
#             print(arr[i][j], end = ' ')
#         else :
#             print(arr[i][-j-1], end = ' ')
#     print()






def iswall(x,y):   # 연습문제
    if x < 0 or x>=5:
        return True
    if y < 0 or y>=5:
        return True
    return False

arr1 = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]
    ]

dx = [0, 0 , -1, 1]
dy = [-1, 1, 0, 0]

summ = 0
for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        for k in range(4):
            testX = i + dx[k]
            testY = j + dy[k]
            if iswall(testX, testY) == False:
                summ += abs(arr1[testX][testY] - arr1[i][j])


print(summ)


