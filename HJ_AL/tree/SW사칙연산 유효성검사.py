import sys
sys.stdin = open("사칙연산.txt")

def input_data(args):
    #print(args)
    if len(args) == 2:
        args.append(None)
        args.append(None)
    if len(args) == 3:
        args.append(None)
    chr.append(args[1])
    data[args[0]] = [args[2], args[3]]

def inorder(root='1'):
    temp = root
    #print(temp)
    if data[temp][0] == None:
        stack.append(chr[int(temp)-1])
        return True
    inorder(data[temp][0])
    stack.append(chr[int(temp)-1])
    if data[temp][1] != None:
        inorder(data[temp][1])

# def cal():
#     result_cal = []
#     operater = ['+', '-', '/', '*']
#     while len(chr)>0:
#         temp = chr.pop(0)
#         result_cal.append(temp)
#         if result_cal[-1] not in operater: # 숫자
#             if len(result_cal)>2 and
#
#
#         else:

def isok():
    operater = ['+', '-', '/', '*']
    if stack[0] in operater:
        return False
    for i in range(1,len(chr)):
        if stack[i-1] in operater and stack[i] in operater:
            return False
    return True


for _ in range(10):
    num = int(input())  # 노드 수
    data = {}
    chr=[]
    for i in range(num):
        #print(i)
        input_data(list(map(str,input().split())))
    #print(data)
    #print(chr)
    stack =[]
    inorder()
    print(f"#{_+1} {int(isok())}")
    #print(stack)