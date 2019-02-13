import sys
sys.stdin = open("사칙연산.txt")

def input_data(args):
    print(args)
    if len(args) == 2:
        args.append(None)
        args.append(None)
    if len(args) == 3:
        args.append(None)
    data[(args[0], args[1])] = [args[2], args[3]]


for _ in range(10):
    num = int(input())  # 노드 수
    data = {}
    for i in range(num):
        print(i)
        input_data(list(map(str,input().split())))

    print(data)