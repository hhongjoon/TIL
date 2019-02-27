T = int(input())
data = []
for i in range(T):
    data.append((input().split()))

result = 'F'
for i in range(len(data)):
    if data[i][1] == 'Y':
        if result != 'F' and result < int(data[i][0]): # 숫자이고 기본 값이 더작으면 continue
            continue
        result = int(data[i][0]) # 처음 들어오면 저장

    else:
        if result !='F' and result <= int(data[i][0]):  #
            result='F'
            break


print(result)