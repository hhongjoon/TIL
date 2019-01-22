# arr = [0]*10
# for i in range(10):
#     arr[i] = [0]*10

import sys
sys.stdin = open("색칠하기_input.txt")

def calculate(data):
    for i in range(len(data)):

        for a in range(data[i][0], data[i][2]+1):
            for b in range(data[i][1],data[i][3]+1):
                #print(a, b)
                if arr[a][b] == 0 :
                    arr[a][b] += data[i][4]
                elif (arr[a][b] == 1 and data[i][4] == 2)  or  (arr[a][b] == 2 and data[i][4] == 1):

                    arr[a][b] += data[i][4]
                else:
                    continue
    result = 0
    for i in arr:
        result += i.count(3)
    return result





casecount = int(input())
for i in range(casecount):
    ea = int(input())
    data = [0]*ea
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for j in range(ea):
        data[j] = list(map(int, input().split()))

    print(f"#{i+1} {calculate(data)}")

