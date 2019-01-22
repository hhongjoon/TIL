def array_sum(a):
    sum_diagonal = 0
    sum_reverse = 0
    sum_row = 0
    sum_col = 0
    for i in range(len(a)):
        sum_diagonal += a[i][i]
    print(sum_diagonal, 'dia')


    for reverse_i in range(len(a)):
        sum_reverse += a[reverse_i][len(a)-1 - reverse_i]

    print(sum_reverse, 'reverse')

    for row in range(len(a)):

        if sum_row < sum(a[row]):
            sum_row = sum(a[row])

    print(sum_row, 'row')

    for col in range(len(a)):
        temp = 0
        for row in range(len(a)):
            temp += a[row][col]

            if sum_col < temp:
                sum_col = temp
    print(sum_col, 'col')
    return max(sum_diagonal, sum_row, sum_col, sum_reverse)



import sys
sys.stdin = open("array_sum.txt")
data = [0]*100
for i in range(10):
    count = int(input())

    for j in range(100):
        data[j] = list(map(int, input().split()))
    print(f"#{i+1} {array_sum(data)}")