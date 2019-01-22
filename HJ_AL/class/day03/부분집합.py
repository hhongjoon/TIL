# bit = [0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             print(bit)

arr = [1,2,3]
n = len(arr)
print(2<<n)      ## 10진수 수를 비트연산자로 계산
for i in range(1<<n):
    for j in range(n):
        print(i , j , i<<j ,'cc')
        if i & (i << j):
            print(arr[j], end=',')
    print()

















    

arr = [-7, -3, -2, 5, 8]
# for i in
