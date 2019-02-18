import sys
sys.stdin = open("트리사칙연산.txt")

def solve(node):
    print(node)

    if node == None:
        return True
    print(tree_struc[node][0])
    print(node_val[int(tree_struc[node][0])])
    if node_val[tree_struc[node][0]].isdigit() and node_val[tree_struc[node][1]].isdigit():
        if node == '+':
            node_val[int(node)] = (int(node_val(tree_struc[node][0])) + int(node_val(tree_struc[node][1])))
        if node == '-':
            node_val[int(node)] =(int(node_val(tree_struc[node][0])) - int(node_val(tree_struc[node][1])))
        if node == '*':
            node_val[int(node)] =(int(node_val(tree_struc[node][0])) * int(node_val(tree_struc[node][1])))
        if node == '/':
            node_val[int(node)] =(int(node_val(tree_struc[node][0])) / int(node_val(tree_struc[node][1])))
        return True


    solve(tree_struc[node][0])
    saveVal.append(node_val[int(node)])
    if tree_struc[node][1] !=None:
        solve(tree_struc[node][1])


def result(saveVal):
    pivot = int(saveVal[0])
    operator = ['+','-','*','/']
    for i in range(1,len(saveVal)):
        if i in operator:
            continue
        else:
            if saveVal[i-1] == '+':
                pivot = pivot + int(saveVal[i])
            if saveVal[i-1] == '-':
                pivot = pivot - int(saveVal[i])
            if saveVal[i-1] == '*':
                pivot = pivot * int(saveVal[i])
            if saveVal[i-1] == '/':
                pivot = pivot / int(saveVal[i])
    return pivot





for _ in range(10):
    nums = int(input())
    node_val = ['no']  # 초기값 1부터 시작하도록  # 자리값마다 값
    tree_struc = {}  # 트리구조를 딕셔너리로
    for i in range(nums):

        input_data = list(input().split())
        if len(input_data) == 3:
            input_data.append(None)
        if len(input_data) == 2:
            input_data += [None, None]
        node_val.append(input_data[1])
        tree_struc[input_data[0]] = [input_data[2],input_data[3]]
    print(tree_struc)
    print(node_val)
    saveVal = []
    solve('1')
    print(saveVal)
    print(result(saveVal))