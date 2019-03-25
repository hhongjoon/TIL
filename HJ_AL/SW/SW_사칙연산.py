def postorder(num):
    if num == '-1':
        return

    val = path[int(num)][1]
    if val in operators:
        if val == '+':
            path[int(num)][1] = int(postorder(path[int(num)][2])) + int(postorder(path[int(num)][3]))
        if val == '-':
            path[int(num)][1] = int(postorder(path[int(num)][2])) - int(postorder(path[int(num)][3]))
        if val == '*':
            path[int(num)][1] = int(postorder(path[int(num)][2])) * int(postorder(path[int(num)][3]))
        if val == '/':
            path[int(num)][1] = int(postorder(path[int(num)][2])) / int(postorder(path[int(num)][3]))

    else:
        return val

    return path[int(num)][1]

for _ in range(10):
    ea = int(input())
    path = [['0']]
    for i in range(ea):
        path.append(list(input().split()))
    # print(path)
    for i in range(ea):
        while len(path[i])<4:
            path[i].append('-1')
    # print(path)
    operators = ['+','-','*','/']
    print("#{} {}".format(_+1,int(postorder('1'))))
