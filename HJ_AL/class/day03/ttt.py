def array_sum(a):
    sum_diagonal = sum_reverse = sum_row = sum_col = 0

    sum_diagonal = sum([a[i][i] for i in range(len(a))])
    print(sum_diagonal, 'd')
    sum_reverse = sum([a[reverse_i][len(a)-1 - reverse_i]for reverse_i in range(len(a))])
    print(sum_reverse, 'reverse')
    sum_row = [ sum(a[row]) for row in range(len(a)) if sum_row < sum(a[row])]
    print(sum_row[-1], 'row')
    for col in range(len(a)):
        temp = 0
        for row in range(len(a)):
            temp += a[row][col]
            if sum_col < temp:
                sum_col = temp
    print(sum_col, 'c')
    return max(sum_diagonal, sum_row[-1], sum_col, sum_reverse)
import sys
sys.stdin = open("array_sum.txt")
data = [0]*100
for i in range(10):
    count = int(input())
    for j in range(100):
        data[j] = list(map(int, input().split()))
    print(f"#{i+1} {array_sum(data)}")